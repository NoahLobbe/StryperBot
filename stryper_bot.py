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
DEBUG = True

JSON_INDENTS = 4
DATA_FILE = "data.json"

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

load_dotenv()

def getToken():
    BOT_TOKEN = os.getenv('STRYPER_BOT_TOKEN')
    assert BOT_TOKEN is not None
    return BOT_TOKEN

def loadPrivilegedMembers():
    privileged_member_names_str = os.getenv('PRIVILEGED_MEMBER_NAMES')
    assert privileged_member_names_str is not None

    privileged_member_names = privileged_member_names_str.split(',')
    
    for name in privileged_member_names:
        PRIVILEGED_MEMBERS.add(name)

    #print(f"PRIVILEGED_MEMBERS: {PRIVILEGED_MEMBERS}")

async def getChannel(DEBUG=True):
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
    for k, v in Dict.items(): 
        if v == value:
            return k


### Setup functions
def DataFileExists():
    """Returns True if already existed, and False if file had to be made"""
    if not os.path.exists(DATA_FILE):
        print(f"Making '{DATA_FILE}'")
        with open(DATA_FILE, "w+") as new_file:
            data = {"songs": []}
            json.dump(data, new_file, indent=JSON_INDENTS)
        return False
    return True



### Functions for bot
##validate if a user provide url is a stryper youtube video
def isYoutube(url):
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
    is_valid_url = bool(validators.url(url))
    if is_valid_url:
        return isYoutube(url)       
    else:
        return False, ""
    

def cleanYoutubeURL(url):
    cut_off_index = url.find("&") #first one found is returned, which is the start of extra needless data in url
    return url[:cut_off_index]


def validateRating(rating_str):
    try:
        rating = float(rating_str)
        if (rating).is_integer():
            rating = int(rating) #makes the text output later nicer :D
        return (rating >= 0 and rating <= 10)
    except ValueError as e:
        print(e)
        return False



### songs function
def loadSongs():
    with open(DATA_FILE, "r") as read_file:
        return json.load(read_file)
    

def songMessage(song_dict):
    intro = "***Hello everybody and WELCOME to Stryper Saturday!!!***" 
    description = f"\nToday is the amazing song *{song_dict['title']}*, with a rating of {song_dict['rating']}/10: "
    link = song_dict["url"]
    notes = song_dict["notes"]
    return intro + description + link, notes


def doesSongExist(songs_json, song_dict):
    for song in songs_json["songs"]:
        if ((song_dict["url"] == song["url"]) or (song_dict["title"] == song["title"])):
            print("already exists!")
            return True
    return False

   
def addSong(title, url, rating, notes):
    new_song = {"title":title, "url":url, "rating":rating, "notes":notes}
    current_songs_json = loadSongs()

    if not doesSongExist(current_songs_json, new_song):
        with open(DATA_FILE, "w") as write_file:
            current_songs_json["songs"].append(new_song) #updated

            json.dump(current_songs_json, write_file, indent=JSON_INDENTS)
        return True
    return False


def getSong(index):
    songs_json = loadSongs()
    return songs_json["songs"][index]


def _getRandomSong():
    songs_json = loadSongs()
    song = rand.choice(songs_json["songs"])
    print(f"Random song: {song}")
    return song



##Bot functions
async def isMemberPrivileged(context):
    ctx_message = context.message
    return ctx_message.name in PRIVILEGED_MEMBERS


async def postSong(CHANNEL, song):
    msg, note = songMessage(song)
    await CHANNEL.send(msg)
    if note != "": await CHANNEL.send(note)


@discord.ext.tasks.loop(seconds=30)
async def chirp(msg=""):
    print(CHANNEL, type(CHANNEL))
    await CHANNEL.send("chirp" + msg)
    print("chirped" + msg)



## Bot functions for determining when to trigger (enact Stryper Saturday) :D
@discord.ext.tasks.loop(time=TRIGGER_TIME)
async def trigger():
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
    msg = f"I, {Bot.user.name}, am alive!"
    await context.send(msg)
    print(msg)
    print(context.message)

@Bot.command()
async def greet(context):   
    is_member_allowed = await isMemberPrivileged(context) 
    if is_member_allowed:
        await context.send("Why hello there!")


@Bot.command()
async def random(context):
    song = _getRandomSong()
    await postSong(context, song)


@Bot.command()
async def add(context, *arguements):
    print(f"User inputted: {arguements}")

    youtube_url = arguements[0]
    rating = arguements[1]

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
    if len(arguements) > 2:
        notes = " ".join(arguements[2:])
        
    is_success = addSong(yt_title, clean_yt_url, rating, notes)
    if is_success:
        await postSong(context, getSong(-1))
        print("...successful")
    else:
        error_msg = "Already added! Update entry using .update command"
        await context.send(error_msg)
        print(error_msg)


@Bot.command()
async def update(context):
    await context.send("command currently not supported...")


@Bot.event
async def on_ready():
    global CHANNEL

    loadPrivilegedMembers()
    CHANNEL = await getChannel(DEBUG)

    #prints
    print(f"{Bot.user} has connected to Discord, into '{CHANNEL}' channel!")
    await CHANNEL.send(TRIGGER_SETUP_MSG)
    print(TRIGGER_SETUP_MSG)

    #loop functions
    await trigger.start()

    

    
if __name__ == "__main__":
    already_existed = DataFileExists()
    if not already_existed:
        default_song = ("To Hell with the Devil", 
                        "https://www.youtube.com/watch?v=sG0zAn0dL2I", 
                        10, 
                        "Containing 4 minutes of legenedary epicness, it will get you **pumped**!")
        addSong(*default_song)

    #print("loading", loadSongs())

    try:
        Bot.run(getToken())

    except aiohttp.client_exceptions.ClientConnectorError as e:
        print(f"...oops I caught a connection error running the bot: \n\t{e}")
