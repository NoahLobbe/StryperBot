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
TRIGGER_TIME = datetime.time(hour=22, minute=36, tzinfo=TIMEZONE) 
TRIGGER_DAY_STR = "Saturday"
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
        privileged_members_list.insert(0, author_name)

    PRIVILEGED_MEMBERS = set(privileged_members_list)
    AUTHOR = set(author_name) #don't want it mutable

    #print(f"PRIVILEGED_MEMBERS: {PRIVILEGED_MEMBERS}")


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
    return is_youtube, title


def validateYoutubeURL(url):
    """Returns bool as to whether 'url' <str> is legit 
    and if it is actually a youtube video link"""
    is_valid_url = bool(validators.url(url))
    if is_valid_url:
        return isYoutube(url)       
    else:
        return False, ""
    

def cleanYoutubeURL(url):
    """Gets rid of extra unneccessary data in URL"""
    cut_off_index = url.find("&") #first one found is returned, which is the start of extra needless data in url
    return url[:cut_off_index]


def validateRating(rating_str):
    """Returns bool as to whether rating is valid"""
    try:
        rating = float(rating_str)
        if (rating).is_integer():
            rating = int(rating) #makes the text output later nicer :D
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
    new_string = template
    replacements = [
        ("{title}", song["title"]),
        ("{url}",song["url"]),
        ("{rating}", str(song['rating'])), #has to be a str for .replace(...)
        ("{notes}", song["notes"])
    ]
    for replacement in replacements:
        new_string = new_string.replace(replacement[0], replacement[1])
    return new_string

        





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

    template = randomTemplate()
    body = _insertSongToTemplate(template, song)
    notes = song["notes"]

    return body, notes
    



def doesSongExist(songs_list:list, song:dict):
    """Returns bool"""
    for s in songs_list:
        if ((song["url"] == s["url"]) or (song["title"] == s["title"])):
            print("already exists!")
            return True
    return False

   
def addSong(title, url, rating, notes):
    """Returns False if song already exists, and True if successful in adding song"""
    new_song = {"title":title, "url":url, "rating":rating, "notes":notes}

    current_data_file = getDataFile()
    current_songs_list = current_data_file["songs"]

    if not doesSongExist(current_songs_list, new_song):
        with open(DATA_FILE, "w") as write_file:
            current_songs_list.append(new_song) #should also update current_data_file, right?

            json.dump(current_data_file, write_file, indent=JSON_INDENTS)
        return True
    return False


def getSong(index):
    """Returns a song <dict> of the given index in database"""
    songs_list = getSongs()
    return songs_list[index]


def _getRandomSong():
    "Returns a song <dict>"
    songs_list = getSongs()
    song_dict = rand.choice(songs_list)
    #print(f"Random song: {song_dict}")
    return song_dict



### Bot functions (not 'slash' commands)
async def isMemberPrivileged(context):
    """Returns bool"""
    ctx_message = context.message
    return ctx_message.name in PRIVILEGED_MEMBERS


async def postSong(context, song:dict):
    """Uses the 'song' <dict> to make prettier text to post to 'context'"""
    msg, note = songMessage(song)
    await context.send(msg)
    if note != "": await CHANNEL.send(note)

'''
@discord.ext.tasks.loop(seconds=30)
async def chirp(msg=""):
    print(CHANNEL, type(CHANNEL))
    await CHANNEL.send("chirp" + msg)
    print("chirped" + msg)
'''


@discord.ext.tasks.loop(time=TRIGGER_TIME)
async def trigger():
    """'Triggers' everyday at a certain time, but only properly triggers if today is the correct day"""
    day = datetime.datetime.now().weekday()
    if day == TRIGGER_DAY_NUM:
        msg = "Triggering..."
    else:
        day_str = getKey(DAYS_LEGEND, day) 
        msg = f"Wrong day to trigger as today is {day_str} not {TRIGGER_DAY_STR} \n:("

    print(msg)



### 'slash' commands (prefix defined in Bot constructor)
@Bot.command()
async def alive(context):
    """Simple test slash command to determine if Bot is operating. Anybody can run this."""
    msg = f"I, {Bot.user.name}, am alive!"
    await context.send(msg)
    print(msg)
    print(context.message)

"""
@Bot.command()
async def greet(context):   
    is_member_privileged = await isMemberPrivileged(context) 
    if is_member_privileged:
        await context.send("Why hello there!")
"""


@Bot.command()
async def random(context):
    """Posts a random song from database, provided the member to call random has the privilege"""
    is_member_privileged = await isMemberPrivileged(context) 
    if is_member_privileged:
        song = _getRandomSong()
        await postSong(context, song)


@Bot.command()
async def add(context, youtube_url, rating, *raw_notes):
    """Adds song to database. 'rating' needs to be a positive integer from 0 to 10,
    and 'raw_notes' is just in case some adds song notes without quotes, as discord.py
    seems to split arguements by spaces."""

    print(f"User inputted: '{youtube_url}', '{rating}', and '{raw_notes}'")

    #validate user input
    url_is_legit, yt_title = validateYoutubeURL(youtube_url)
    rating_is_legit = validateRating(rating)

    url_invalid_str = f"'{youtube_url}' is not reachable"
    rating_invalid_str = f"'{rating}' is invalid, has to be a positive integer from 0 to 10"
    
    #output stufff
    if url_is_legit and rating_is_legit:
        msg = "URL and rating are valid..."
    elif url_is_legit and not rating_is_legit:
        msg = rating_invalid_str
    elif not url_is_legit and rating_is_legit:
        msg = url_invalid_str
    else:
        msg = url_invalid_str + ", and " + rating_invalid_str 
    print(msg)
    await context.send(msg)

    #prep and add song to songs file
    clean_yt_url = cleanYoutubeURL(youtube_url)
    notes = ""
    if len(raw_notes) > 2:
        notes = " ".join(raw_notes[2:])
        
    is_success = addSong(yt_title, clean_yt_url, rating, notes)
    if is_success:
        await postSong(context, getSong(-1))
        print("...successful")
    else:
        error_msg = "Already added! Update entry using .update command"
        await context.send(error_msg)
        print(error_msg)


@Bot.event
async def on_ready():
    """Runs when Bot is ready, kind of like a class constructor/init/"""
    #setup variables
    global CHANNEL
    CHANNEL = await getChannel(IS_DEBUGGING) 

    loadPrivilegedMembers()

    already_existed = DataFileExists()

    #test (delte later)
    song = _getRandomSong()
    msg, notes = songMessage(song)
    print(msg, "\n" + notes)




    #prints
    print(f"{Bot.user} has connected to Discord, into '{CHANNEL}' channel!")
    await CHANNEL.send(TRIGGER_SETUP_MSG)
    print(TRIGGER_SETUP_MSG)

    if not already_existed:
        msg = "ERROR: database is empty, please fill..."
        await CHANNEL.send(msg)
        print(msg)

    #loop functions
    await trigger.start()



    

    
if __name__ == "__main__":
    load_dotenv()  #enable os.getenv() to actually get 'environment variables' from .env file

    try:
        Bot.run(getBotToken())

    except aiohttp.client_exceptions.ClientConnectorError as e:
        print(f"...oops I caught a connection error running the bot: \n\t{e}")
