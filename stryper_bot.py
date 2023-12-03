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
TRIGGER_TIME = datetime.time(hour=19, minute=29, tzinfo=TIMEZONE) 
TRIGGER_DAY_STR = "Saturday" #"Saturday"
TRIGGER_DAY_NUM =   DAYS_LEGEND[TRIGGER_DAY_STR]
TRIGGER_SETUP_MSG = f"Trigger time set for {TRIGGER_DAY_STR} @ {TRIGGER_TIME.strftime('%H:%M')}" 

#bot setup
BotIntents = discord.Intents.default()
BotIntents.message_content = True 
Bot = discord.ext.commands.Bot(command_prefix=".", intents=BotIntents)

CHANNEL = None #the channel to post messages into
PRIVILEGED_MEMBERS = set() #wanted something immutable
AUTHOR = set()


###Secrets helper functions
def _getBotToken():
    """Returns str"""
    BOT_TOKEN = os.getenv("STRYPER_BOT_TOKEN")
    assert BOT_TOKEN is not None
    return BOT_TOKEN


def _loadPrivilegedMembers():
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


async def _getChannel(debug_mode=True):
    """Returns a discord.py Channel object to be used"""
    if debug_mode:
        channel_id_str = os.getenv('DEBUG_CHANNEL_ID')
    else:
        channel_id_str = os.getenv('DEPLOYED_CHANNEL_ID')
    channel_id = int(channel_id_str)

    channel = Bot.get_channel(channel_id)
    #print(f"_getChannel(): {channel_id}, {channel}")
    return channel

    

### Miscen... helper functions
def _getDictKey(Dict, value):
    """Returns key from the key:value pair in a dict"""
    for k, v in Dict.items(): 
        if v == value:
            return k



### User input (parsing?) helper functions
def _isYoutube(url):
    """Returns bool and str. Bool for whether 'url' (str) is a youtube video url,
    and str of the youtube video's title if it is legit."""
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
    

def _cleanYoutubeURL(url):
    """Returns str. Gets rid of extra unneccessary data in url (str)"""
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


def _validateYoutubeURL(url):
    """Returns bool as to whether 'url' (str) is legit 
    and if it is actually a youtube video link"""
    clean_url = _cleanYoutubeURL(url)
    is_valid_url = bool(validators.url(clean_url))
    if is_valid_url:
        print(f"valid URL is cleaned to: {clean_url}")
        is_youtube, yt_title = _isYoutube(clean_url)
        return is_youtube, yt_title, clean_url       
    else:
        return False, "", clean_url


def _validateRating(rating_str):
    """Returns bool as to whether rating is valid"""
    try:
        rating = float(rating_str)
        if (rating).is_integer():
            rating = int(rating) #makes the text output nicer later :D
        return (rating >= 0 and rating <= 10)
    except ValueError as e:
        print(e)
        return False



### Data file helper function(s)
def _doesDataFileExist():
    """Returns bool. True if already existed, and False if file had to be made"""
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


def _getData():
    """Returns JSON object of whole file"""
    with open(DATA_FILE, "r") as read_file:
        return json.load(read_file)



### Templates helper functions
def _getTemplates():
    """Returns a list of templates"""
    with open(DATA_FILE, "r") as read_file:
        return json.load(read_file)["templates"]
    
def _writeTemplates(new_template):
    """Writes templates to database"""
    current_database = _getData()
    current_templates_list = current_database["templates"]

    with open(DATA_FILE, "w") as write_file:
        current_templates_list.append(new_template)

        json.dump(current_database, write_file, indent=JSON_INDENTS)

    
def _randomTemplate():
    """Returns str"""
    templates = _getTemplates()
    if len(templates) > 0:
        return rand.choice(_getTemplates())
    else:
        default = "***Hello everybody and WELCOME to Stryper Saturday!!!*** \nToday is the amazing song *{title}*, with a rating of {rating}/10: {url}" 
        _writeTemplates(default)
        return default


def _insertSongToTemplate(template, song):
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

        
def _isValidTemplate(raw_template):
    """Returns bool"""
    has_title = "{title}" in raw_template
    has_rating = "{rating}" in raw_template
    has_url = "{url}" in raw_template

    return (has_title and has_rating and has_url), (has_title, has_rating, has_url)


def _doesTemplateExist(templates_list, template):
    """Returns (bool, int). True if already exists, int of index if it exists, 0 otherwise."""
    for i, t in enumerate(templates_list):
        if (t == template):
            print("exists!")
            return True, i
    return False, 0

def _addTemplate(new_template):
    """Returns bool. True if successful, False otherwise"""
    
    current_data_file = _getData()
    current_templates_list = current_data_file["templates"]

    template_already_exists, index = _doesTemplateExist(current_templates_list, new_template)
    if not template_already_exists:
        
        current_data_file["templates"].append(new_template)

        with open(DATA_FILE, "w") as write_file:    
            json.dump(current_data_file, write_file, indent=JSON_INDENTS)
        
        return True
    return False




### songs helper functions
def __getSongs():
    """Returns list of songs"""
    with open(DATA_FILE, "r") as read_file:
        return json.load(read_file)["songs"]
    

def _songMessage(song):
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

    template = _randomTemplate()
    body = _insertSongToTemplate(template, song)
    notes = song["notes"]

    return body, notes
    



def _doesSongExist(songs_list, song_url):
    """Returns (bool, int). 
    Bool for the existence of song in database, and int of index of existing song.
    If song doesn't exist, then index is 0. Based on 'song_url' (str)"""
    print(f"in _doesSongExist(), song_url: {song_url} ")
    for i, s in enumerate(songs_list):
        if (song_url == s["url"]):
            print("exists!")
            return True, i
    return False, 0

   
def _addSong(title, url, rating, notes):
    """Returns True if successful in adding the song to database or overwriting if""" ##################################finish
    new_song = {"title":title, "url":url, "rating":rating, "notes":notes}
    print(f"in addSong(), url: {new_song['url']}")

    current_data_file = _getData()
    current_songs_list = current_data_file["songs"]

    song_already_exists, index_of_song = _doesSongExist(current_songs_list, new_song["url"])
    if not song_already_exists:
        #add song to database
        with open(DATA_FILE, "w") as write_file:
            current_songs_list.append(new_song) #should also update current_data_file, right?

            json.dump(current_data_file, write_file, indent=JSON_INDENTS)
        return True
    else:
        return False
    
def _updateSong(song_url, new_rating, new_notes):
    """Updates song rating and notes in database if it exists. Returns bool of success/failure, messsage str"""    
    current_data_file = _getData()
    current_songs_list = current_data_file["songs"]

    song_already_exists, index_of_song = _doesSongExist(current_songs_list, song_url)

    if song_already_exists:
        rating_is_legit = _validateRating(new_rating)
        if rating_is_legit:
            #update song entry    
            current_songs_list[index_of_song]["rating"] = new_rating
            current_songs_list[index_of_song]["notes"] = new_notes

            with open(DATA_FILE, "w") as write_file:
                json.dump(current_data_file, write_file, indent=JSON_INDENTS)
            return True, "success"
        return False, "invalid rating"
    return False, "doesn't exist"


def _getSong(index):
    """Returns a song dict of the given index in database"""
    songs_list = __getSongs()
    return songs_list[index]


def _getRandomSong():
    "Returns a song dict"
    songs_list = __getSongs()
    song_dict = rand.choice(songs_list)
    return song_dict



### Bot functions (not 'slash' commands)
async def isMemberPrivileged(Context):
    """Returns bool"""
    ctx_message = Context.message
    return ctx_message.author.name in PRIVILEGED_MEMBERS


async def postSong(Context, song):
    """Uses the 'song' (dict) to make prettier text to post to 'Context'"""
    msg, note = _songMessage(song)
    await Context.send(msg)
    if note != "": await CHANNEL.send(note)


async def addSong(Context, title, url, rating, raw_notes):
    """Returns bool of success/failure"""
    #prep and add song to songs file        
    notes = ""
    if len(raw_notes) > 2:
        notes = " ".join(raw_notes[2:])
        
    is_success = _addSong(title, url, rating, notes)
    if is_success:
        await postSong(Context, _getSong(-1))
        print("...successful")
        return True
    else:
        error_msg = "Already added! Update entry using .update command"
        await Context.send(error_msg)
        print(error_msg)
        return False


async def messageIsStryperDay(Context, Message):
    """Returns bool"""
    #does message mention Stryper Day?
    is_mentioned = "Stryper Saturday" in Message.content

    does_contain_link = False
    if does_contain_link:
        link_is_stryper = False



@discord.ext.tasks.loop(time=TRIGGER_TIME)
async def trigger(channel):
    """'Triggers' everyday at a certain time, but only properly triggers if today is the correct day"""
    DateNow = datetime.datetime.now()
    day_num = DateNow.weekday()
    if day_num == TRIGGER_DAY_NUM:
        song = _getRandomSong()
        await postSong(channel, song)
        print("Triggered")

        #"""
        #get messages from today
        year = DateNow.year
        month = DateNow.month
        day = DateNow.day
        tzinfo = TIMEZONE
        AfterDate = datetime.datetime(year=year, month=month, day=day, tzinfo=tzinfo)

        print(f"AfterDate: {AfterDate}")

        Msg_Iter = channel.history(after=AfterDate, oldest_first=False)

        enacted_bit_map = []

        for Msg in Msg_Iter:
            #is SS enacted for Msg??
            print(f"author: {Msg.author}  | content: {Msg.content}")

        already_enacted = True in enacted_bit_map

        if not already_enacted:
            pass #enact
        else:
            pass #reply with a 'oo-rah!!!' kinda of message??? (REPLY @ ENACT-TOR)



        print(f"AfterDate: {AfterDate}")

        
        #"""
    else:
        day_str = _getDictKey(DAYS_LEGEND, day) 
        msg = f"Wrong day to trigger as today is {day_str} not {TRIGGER_DAY_STR} \n:("

        await CHANNEL.send(msg)
        print(msg)



### 'slash' commands (prefix defined in Bot constructor)
@Bot.command()
async def alive(Context):
    """Simple test slash command to determine if Bot is operating. Anybody can call this."""
    msg = f"*I AM ALIVE!!!*"
    await Context.send(msg)
    print(msg)


@Bot.command()
async def random(Context):
    """Posts a random song from database, provided the member to call random has the privilege"""
    is_member_privileged = await isMemberPrivileged(Context) 
    if is_member_privileged:
        song = _getRandomSong()
        await postSong(Context, song)
        print(f"Random song is: {song}")


@Bot.command()
async def add(Context, youtube_url, rating, *raw_notes):
    """Adds song to database. 'rating' needs to be a positive float (decimal) from 0 to 10,
    and 'raw_notes' is just in case some adds song notes without quotes, as discord.py
    seems to split arguements by spaces."""

    is_member_privileged = await isMemberPrivileged(Context) 
    if is_member_privileged:

        print(f"User inputted: '{youtube_url}', '{rating}', and '{raw_notes}'")

        #validate user input
        # moved cleaning the URL into _validateYoutubeURL: clean_yt_url = _cleanYoutubeURL(youtube_url)
        url_is_legit, yt_title, clean_yt_url = _validateYoutubeURL(youtube_url)
        rating_is_legit = _validateRating(rating)
        
        #output stuff
        if url_is_legit and rating_is_legit:
            is_successful = await addSong(Context, yt_title, clean_yt_url, rating, raw_notes)
            if is_successful:
                await Context.send("\nAdded!")

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
            await Context.send(msg)


@Bot.command()
async def update(Context, song_url, new_rating, *new_notes):
    """Updates database provided the song_url is in the database"""
    is_member_privileged = await isMemberPrivileged(Context) 

    if is_member_privileged:
        url_is_legit, _, clean_url = _validateYoutubeURL(song_url)

        if url_is_legit:
            is_successful, status_msg = _updateSong(clean_url, new_rating, new_notes)

            if is_successful:
                msg = status_msg
            else:
                msg = f"ERROR: {status_msg}"  

        else:
            is_url_suppressed = ('<' in song_url) and ('>' in song_url)
            url = (is_url_suppressed * '<') + song_url + (is_url_suppressed * '>')
            msg = f"ERROR: invalid url passed, '{url}'"

        await Context.send(msg)
        print(msg) 


@Bot.command()
async def add_template(Context, *raw_new_template_parts):
    """Add a template string to database"""
    is_member_privileged = await isMemberPrivileged(Context) 
    if is_member_privileged:
        #print(raw_new_template_parts)
        new_template = " ".join(raw_new_template_parts)
        is_valid, code_bools = _isValidTemplate(new_template)

        if is_valid:
            is_successful = _addTemplate(new_template)
            if is_successful:
                msg = "Success"
            else:
                msg = "Template already exists!"
            await Context.send(msg)
            print(msg)
            
                
        else:
            msg = f"ERROR in '{new_template}':"
            #determine error message based on `code_bools`
            if not code_bools[0]:
                msg += "\n\tRequires title code '{title}'"
            if not code_bools[1]:
                msg += "\n\tRequires rating code '{rating}'"
            if not code_bools[2]:
                msg += "\n\tRequires url code '{url}'"
            
            await Context.send(msg)
            print(msg)



@Bot.command()
async def remove_template(Context):
    """Remove a template string from database"""
    is_member_privileged = await isMemberPrivileged(Context) 
    if is_member_privileged:
        pass #really not sure how to implement this


@Bot.event
async def on_message(Message):
    print("someone sent a message!!!!", Message.content, Message.channel, type(Message.channel))

    #also check previoust couple messages as the Stryper link is usually separate
    num_prev_to_check = 2
    _msg_iter = Message.channel.history(limit=num_prev_to_check, oldest_first=False)
    previous_messages_list = [msg for msg in _msg_iter]

    print(f"_msg_iter: {_msg_iter}, list: {previous_messages_list}")

    stryper_mentioned = False
    stryper_link_present = False
    stryper_title_in_msg_and_link = False
    
    for Msg in _msg_iter:
        if True:
            stryper_link_present = True

        if True:
            stryper_mentioned = True

    # every stryper saturday has a Stryper URL, title, and mention ('Stryper Saturday')
    someone_has_called_stryper_saturday = stryper_link_present and stryper_mentioned and stryper_title_in_msg_and_link


    #if today is trigger day AND message is stryper saturday
        #cancel trigger


@Bot.event
async def on_ready():
    """Runs when Bot is ready, kind of like a class constructor/init/"""
    #setup variables
    global CHANNEL
    CHANNEL = await _getChannel(IS_DEBUGGING) 

    _loadPrivilegedMembers()

    already_existed = _doesDataFileExist()


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
        Bot.run(_getBotToken())

    except aiohttp.client_exceptions.ClientConnectorError as e:
        print(f"...oops I caught a connection error running the bot: \n\t{e}")
