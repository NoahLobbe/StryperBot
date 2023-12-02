"""
GNU General Public License Version 3

Created by Noah Lobbe, November 2023
"""

#standard python libraries
import os
import json
import aiohttp
import datetime
import random as rand

#denpendencies
import discord
import discord.ext.commands
import discord.ext.tasks
import validators
from dotenv import load_dotenv
import requests
from bs4 import BeautifulSoup


###Constants
IS_DEBUGGING = True

JSON_INDENTS = 4
DATA_FILE = "data.json"

# trigger stuff
# Mon==0,...Sun==6 according to datetime.weekday() documentation. Tad messy for stringifying due to the conflict of strftime() and weekday()
DAYS_LEGEND = {"Monday":0, "Tuesday":1, "Wednesday":2, "Thursday":3, "Friday":4, "Saturday":5, "Sunday":6} 

TIMEZONE = datetime.timezone(datetime.timedelta(hours=10.5))  #Adelaide is 10.5 hours ahead of UTC
TRIGGER_TIME = datetime.time(hour=9, minute=50, tzinfo=TIMEZONE) 
TRIGGER_DAY_STR = "Saturday" #"Saturday"
TRIGGER_DAY_NUM =   DAYS_LEGEND[TRIGGER_DAY_STR]
TRIGGER_SETUP_MSG = f"Trigger time set for {TRIGGER_DAY_STR} @ {TRIGGER_TIME.strftime('%H:%M')}" 

#bot setup
botIntents = discord.Intents.default()
botIntents.message_content = True 
Bot = discord.ext.commands.Bot(command_prefix=".", intents=botIntents)

CHANNEL = None #the channel to post messages into
PRIVILEGED_MEMBERS = set() #wanted something immutable
AUTHOR = set()


def getBotToken():
    """Returns token <str>"""
    BOT_TOKEN = os.getenv("STRYPER_BOT_TOKEN")
    assert BOT_TOKEN is not None
    return BOT_TOKEN


def loadPrivilegedMembers():
    """Loads the usernames of discord members who have Bot privileges"""
    global PRIVILEGED_MEMBERS
    #general privileged
    privileged_member_names_str = os.getenv("PRIVILEGED_MEMBER_NAMES")
    assert privileged_member_names_str is not None

    privileged_member_names = privileged_member_names_str.split(',')
    privileged_members_list = []
    
    for name in privileged_member_names:
        privileged_members_list.append(name)

    #get author too.
    author_name = os.getenv("AUTHOR_NAME")
    assert author_name is not None

    if author_name not in privileged_members_list:
        privileged_members_list.append(author_name) #order doesn't matter as it wil be turned into a `set``

    PRIVILEGED_MEMBERS = set(privileged_members_list)
    AUTHOR = set(author_name) #don't want it mutable

    #print(f"PRIVILEGED_MEMBERS (with author): {PRIVILEGED_MEMBERS}")


async def getChannel(DEBUG=True):
    """Returns a discord.py channel object to be used"""
    if DEBUG:
        channel_id_str = os.getenv('DEBUG_CHANNEL_ID')
    else:
        channel_id_str = os.getenv('DEPLOYED_CHANNEL_ID')
    channel_id = int(channel_id_str)

    channel = Bot.get_channel(channel_id)
    #print(f"getChannel(): {channel_id}, {channel}")
    return channel

    

### Miscen... functions
def getKey(Dict, value):
    """Returns key from Dict <dict> for a given 'value'"""
    for k, v in Dict.items(): 
        if v == value:
            return k


### Setup functions
def DataFileExists():
    """Returns True if already existed, and False if file had to be made"""
    if not os.path.exists(DATA_FILE):
        print(f"Making '{DATA_FILE}'")

        with open(DATA_FILE, "w+") as new_file:
            data = {
                "songs": [], 
                "templates":[]
                }
            json.dump(data, new_file, indent=JSON_INDENTS)
        return False
    return True



### Determines
def isYoutube(url:str):
    """Returns bool for whether 'url' <str> is a youtube video url,
    and string of the youtube video's title if is legit."""
    is_youtube = False
    R = requests.get(url)
    html = BeautifulSoup(R.content, features="html.parser")

    for tag in html.find_all("link", attrs={'itemprop':'url'}): #simplest and first spot to find ...
        #print(tag)
        if "href" in tag.attrs.keys(): #HTML tag 'link' would have to have a href right?
            if (tag.attrs['href'] == "http://www.youtube.com/channel/UC20qdRIIoh4Xr6jnmZ4HBng"): #...stryper's official channel URL
                is_youtube = True
    #get title
    title = html.find("meta", attrs={"name":"title"}).attrs["content"]
    print( is_youtube, title)
    return is_youtube, title
    

def cleanYoutubeURL(url):
    """Gets rid of extra unneccessary data in URL"""
    cut_off_index = url.find("&") #first one found is returned, which is the start of extra needless data in url

    if cut_off_index != -1: 
        yt_url = url[:cut_off_index]
    else:
        yt_url = url
    
    #If people want to suppress preview of a link, eg. <link string>, the angle brackets need to be removed
    if yt_url[0] == '<':
        yt_url = yt_url[1:]

    if yt_url[-1] == '>':
        yt_url = yt_url[:-1]

    return yt_url


def validateYoutubeURL(url):
    """Returns bool as to whether 'url' <str> is legit 
    and if it is actually a youtube video link"""
    clean_url = cleanYoutubeURL(url)
    is_valid_url = bool(validators.url(clean_url))
    if is_valid_url:
        print(f"valid URL is cleaned to: {clean_url}")
        is_youtube, yt_title = isYoutube(clean_url)
        return is_youtube, yt_title, clean_url       
    else:
        return False, "", clean_url


def validateRating(rating_str):
    """Returns bool as to whether rating is valid"""
    try:
        rating = float(rating_str)
        if (rating).is_integer():
            rating = int(rating) #makes the text output nicer later :D
        return (rating >= 0 and rating <= 10)
    except ValueError as e:
        print(e)
        return False



### Data file functions
def getDataFile():
    """Returns JSON object of whole file"""
    with open(DATA_FILE, "r") as read_file:
        return json.load(read_file)



### Templates functions
def getTemplates():
    with open(DATA_FILE, "r") as read_file:
        return json.load(read_file)["templates"]
    
def writeTemplates(new_template:str):
    current_database = getDataFile()
    current_templates_list = current_database["templates"]

    with open(DATA_FILE, "w") as write_file:
        current_templates_list.append(new_template)

        json.dump(current_database, write_file, indent=JSON_INDENTS)

    
def randomTemplate():
    templates = getTemplates()
    if len(templates) > 0:
        return rand.choice(getTemplates())
    else:
        default = "***Hello everybody and WELCOME to Stryper Saturday!!!*** \nToday is the amazing song *{title}*, with a rating of {rating}/10: {url}" 
        writeTemplates(default)
        return default


def _insertSongToTemplate(template:str, song:dict):
    """Returns a str which has made o"""

    replacements = [
        ("{title}", song["title"]),
        ("{url}",song["url"]),
        ("{rating}", str(song['rating'])), #has to be a str for .replace(...)
        ("{notes}", song["notes"])
    ]

    new_string = template
    for replacement in replacements:
        new_string = new_string.replace(replacement[0], replacement[1])
    return new_string

        
def isValidTemplate(raw_template:str):
    has_title = "{title}" in raw_template
    has_rating = "{rating}" in raw_template
    has_url = "{url}" in raw_template

    return has_title and has_rating and has_url




### songs function
def getSongs():
    """Returns list of songs"""
    with open(DATA_FILE, "r") as read_file:
        return json.load(read_file)["songs"]
    

def songMessage(song:dict):
    """Returns two strings based on the 'song' <dict>, the first is the main bit, 
    and the second is the notes to be posted afterwards"""
    '''
    intro = "***Hello everybody and WELCOME to Stryper Saturday!!!***" 
    description = f"\nToday is the amazing song *{song['title']}*, with a rating of {song['rating']}/10: "
    link = song["url"]
    notes = song["notes"]
    return (intro + description + link), notes
    '''
    if type(song["notes"]) != str:
        song["notes"] = " ".join(song["notes"]) #concatenate, otherwise a list of the notes will be inserted into template

    template = randomTemplate()
    body = _insertSongToTemplate(template, song)
    notes = song["notes"]

    return body, notes
    



def doesSongExist(songs_list:list, song_url:str):
    """Returns (bool, int). 
    Bool for the existence of song in database, and int of index of existing song.
    If song doesn't exist, then index is 0"""
    print(f"in doesSongExist(), song_url: {song_url} ")
    for i, s in enumerate(songs_list):
        if (song_url == s["url"]):
            print("exists!")
            return True, i
    return False, 0

   
def addSong(title, url, rating, notes):
    """Returns True if successful in adding the song to database or overwriting if"""
    new_song = {"title":title, "url":url, "rating":rating, "notes":notes}
    print(f"in addSong(), url: {new_song['url']}")

    current_data_file = getDataFile()
    current_songs_list = current_data_file["songs"]

    song_already_exists, index_of_song = doesSongExist(current_songs_list, new_song["url"])
    if not song_already_exists:
        #add song to database
        with open(DATA_FILE, "w") as write_file:
            current_songs_list.append(new_song) #should also update current_data_file, right?

            json.dump(current_data_file, write_file, indent=JSON_INDENTS)
        return True
    else:
        return False
    
def updateSong(song_url, new_rating, new_notes):
    """Updates song rating and notes in database if it exists. Returns bool of success/failure"""    
    current_data_file = getDataFile()
    current_songs_list = current_data_file["songs"]

    song_already_exists, index_of_song = doesSongExist(current_songs_list, song_url)

    if song_already_exists:
        rating_is_legit = validateRating(new_rating)
        if rating_is_legit:
            #update song entry    
            current_songs_list[index_of_song]["rating"] = new_rating
            current_songs_list[index_of_song]["notes"] = new_notes

            with open(DATA_FILE, "w") as write_file:
                json.dump(current_data_file, write_file, indent=JSON_INDENTS)
            return True, "success"
        return False, "invalid rating"
    return False, "doesn't exist"


def getSong(index):
    """Returns a song <dict> of the given index in database"""
    songs_list = getSongs()
    return songs_list[index]


def _getRandomSong():
    "Returns a song <dict>"
    songs_list = getSongs()
    song_dict = rand.choice(songs_list)
    return song_dict



### Bot functions (not 'slash' commands)
async def isMemberPrivileged(context):
    """Returns bool"""
    ctx_message = context.message
    return ctx_message.author.name in PRIVILEGED_MEMBERS


async def postSong(context, song:dict):
    """Uses the 'song' <dict> to make prettier text to post to 'context'"""
    msg, note = songMessage(song)
    await context.send(msg)
    if note != "": await CHANNEL.send(note)


async def _random(context):
    song = _getRandomSong()
    await postSong(context, song)
    


async def _addSong(context, title, url, rating, raw_notes):
    #prep and add song to songs file        
        notes = ""
        if len(raw_notes) > 2:
            notes = " ".join(raw_notes[2:])
            
        is_success = addSong(title, url, rating, notes)
        if is_success:
            await postSong(context, getSong(-1))
            print("...successful")
        else:
            error_msg = "Already added! Update entry using .update command"
            await context.send(error_msg)
            print(error_msg)




@discord.ext.tasks.loop(time=TRIGGER_TIME)
async def trigger(channel):
    """'Triggers' everyday at a certain time, but only properly triggers if today is the correct day"""
    day = datetime.datetime.now().weekday()
    if day == TRIGGER_DAY_NUM:
        await _random(channel)
        print("Triggered")
    else:
        day_str = getKey(DAYS_LEGEND, day) 
        msg = f"Wrong day to trigger as today is {day_str} not {TRIGGER_DAY_STR} \n:("

        await CHANNEL.send(msg)
        print(msg)



### 'slash' commands (prefix defined in Bot constructor)
@Bot.command()
async def alive(context):
    """Simple test slash command to determine if Bot is operating. Anybody can call this."""
    msg = f"*I AM ALIVE!!!*"
    await context.send(msg)
    print(msg)


@Bot.command()
async def random(context):
    """Posts a random song from database, provided the member to call random has the privilege"""
    is_member_privileged = await isMemberPrivileged(context) 
    if is_member_privileged:
        await _random(context)


@Bot.command()
async def add(context, youtube_url, rating, *raw_notes):
    """Adds song to database. 'rating' needs to be a positive float (decimal) from 0 to 10,
    and 'raw_notes' is just in case some adds song notes without quotes, as discord.py
    seems to split arguements by spaces."""

    is_member_privileged = await isMemberPrivileged(context) 
    if is_member_privileged:

        print(f"User inputted: '{youtube_url}', '{rating}', and '{raw_notes}'")

        #validate user input
        # moved cleaning the URL into validateYoutubeURL: clean_yt_url = cleanYoutubeURL(youtube_url)
        url_is_legit, yt_title, clean_yt_url = validateYoutubeURL(youtube_url)
        rating_is_legit = validateRating(rating)
        
        #output stuff
        if url_is_legit and rating_is_legit:
            await _addSong(context, yt_title, clean_yt_url, rating, raw_notes)
            await context.send("\nAdded!")

        else:    
            url_invalid_str = f"'{clean_yt_url}' is not reachable"
            rating_invalid_str = f"'{rating}' is invalid, has to be a positive decimal from 0 to 10"

            if url_is_legit and not rating_is_legit:
                msg = rating_invalid_str

            elif not url_is_legit and rating_is_legit:
                msg = url_invalid_str

            else:
                msg = url_invalid_str + ", and " + rating_invalid_str 
                
            print(msg)
            await context.send(msg)


@Bot.command()
async def update(context, song_url, new_rating, *new_notes):
    """Updates database provided the song_url is in the database"""
    is_member_privileged = await isMemberPrivileged(context) 

    if is_member_privileged:
        url_is_legit, _, clean_url = validateYoutubeURL(song_url)

        if url_is_legit:
            is_successful, status_msg = updateSong(clean_url, new_rating, new_notes)

            if is_successful:
                msg = status_msg
            else:
                msg = f"ERROR: {status_msg}"  

        else:
            is_url_suppressed = ('<' in song_url) and ('>' in song_url)
            url = (is_url_suppressed * '<') + song_url + (is_url_suppressed * '>')
            msg = f"ERROR: invalid url passed, '{url}'"

        await context.send(msg)
        print(msg) 


@Bot.command()
async def add_template(context, new_template:str):
    """Add a template string to database"""
    is_member_privileged = await isMemberPrivileged(context) 
    if is_member_privileged:
        is_valid, code_bools = isValidTemplate(new_template)

        if is_valid:
            pass
        else:
            msg = "ERROR: "
            #determine error message based on `code_bools`
            if not code_bools[0]:
                msg += "\n\tRequires title code '{title}'"
            if not code_bools[1]:
                msg += "\n\tRequires rating code '{rating}'"
            if not code_bools[2]:
                msg += "\n\tRequires url code '{url}'"
            
            await context.send(msg)
            print(msg)



@Bot.command()
async def remove_template(context):
    """Remove a template string from database"""
    is_member_privileged = await isMemberPrivileged(context) 
    if is_member_privileged:
        pass


@Bot.event
async def on_ready():
    """Runs when Bot is ready, kind of like a class constructor/init/"""
    #setup variables
    global CHANNEL
    CHANNEL = await getChannel(IS_DEBUGGING) 

    loadPrivilegedMembers()

    already_existed = DataFileExists()


    #prints
    print(f"{Bot.user} has connected to Discord, into '{CHANNEL}' channel!")
    await CHANNEL.send(TRIGGER_SETUP_MSG)
    print(TRIGGER_SETUP_MSG)

    if not already_existed:
        msg = "ERROR: database is empty, please fill..."
        await CHANNEL.send(msg)
        print(msg)

    #loop functions
    await trigger.start(CHANNEL)



    

    
if __name__ == "__main__":
    load_dotenv()  #enable os.getenv() to actually get 'environment variables' from .env file

    try:
        Bot.run(getBotToken())

    except aiohttp.client_exceptions.ClientConnectorError as e:
        print(f"...oops I caught a connection error running the bot: \n\t{e}")
