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
JSON_INDENTS = 4
SONGS_FILE = "songs.json"

TIMEZONE = datetime.timezone(datetime.timedelta(hours=10.5))  #Adelaide is 10.5 hours ahead of UTC
TRIGGER_TIME = datetime.time(hour=15, minute=26, tzinfo=TIMEZONE) 
TRIGGER_DAY_NUM = 2 # Mon==0,...Sun==6 according to datetime documentation (29th Nov 2023)


### Setup functions
def SongsFileExists():
    """Returns True if already existed, and False if file had to be made"""
    if not os.path.exists(SONGS_FILE):
        print(f"Making '{SONGS_FILE}'")
        with open(SONGS_FILE, "w+") as new_file:
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


##songs file stuff
def loadSongs():
    with open(SONGS_FILE, "r") as read_file:
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
        with open(SONGS_FILE, "w") as write_file:
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



###Bot stuff
def load_token():
    load_dotenv()
    BOT_TOKEN = os.getenv('STRYPER_BOT_TOKEN')
    assert BOT_TOKEN is not None
    return BOT_TOKEN

botIntents = discord.Intents.default()
botIntents.message_content = True #enables sending messages?

Bot = discord.ext.commands.Bot(command_prefix=".", intents=botIntents)




##Bot functions

async def postSong(ctx, song):
    msg, note = songMessage(song)
    await ctx.send(msg)
    if note != "": await ctx.send(note)


@discord.ext.tasks.loop(seconds=30)
async def chirp(msg=""):
    StryperBotTesting_id = 1176818000477835295
    guild = Bot.get_guild(StryperBotTesting_id)
    ctx = guild.system_channel
    await ctx.send("chirp" + msg)
    print("chirped" + msg)



## Bot functions for determining when to trigger (enact Stryper Saturday) :D
@discord.ext.tasks.loop(time=TRIGGER_TIME)
async def trigger():
    current_time = datetime.datetime.now()
    if current_time.day == TRIGGER_DAY_NUM:
        print(f"Correct day! ('{current_time.day}') Triggering...")

    else:
        print("Wrong day to trigger ('{current_time.day}') :(")


##'slash' commands (prefix may have been redefined in Bot constructor)
@Bot.command()
async def greet(ctx):    
    print("sending greeting...")
    await ctx.send("Why hello there!")

async def getCTX():
    pass

@Bot.command()
async def random(ctx):
    song = _getRandomSong()
    await postSong(ctx, song)


@Bot.command()
async def add(ctx, *arguements):
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
    await ctx.send(msg)

    #prep and add song to songs file
    clean_yt_url = cleanYoutubeURL(youtube_url)
    notes = ""
    if len(arguements) > 2:
        notes = " ".join(arguements[2:])
        
    is_success = addSong(yt_title, clean_yt_url, rating, notes)
    if is_success:
        await postSong(ctx, getSong(-1))
        print("...successful")
    else:
        error_msg = "Already added! Update entry using .update command"
        await ctx.send(error_msg)
        print(error_msg)


@Bot.command()
async def update(ctx):
    await ctx.send("command currently not supported...")


@Bot.event
async def on_ready():
    #prints
    print(f"{Bot.user} has connected to Discord!")
    print(f"guilds: {Bot.guilds}")
    print(f"channels: {Bot.get_all_channels()}")


    curr = datetime.datetime.now()
    #print(curr.hour == TRIGGER_TIME.hour, curr.minute == TRIGGER_TIME.minute)





    #loop functions
    #await chirp.start("hi!") #just a test function

    await trigger.start()
    
    

    print("finished startup stuff...")

    

    
if __name__ == "__main__":
    already_existed = SongsFileExists()
    if not already_existed:
        default_song = ("To Hell with the Devil", 
                        "https://www.youtube.com/watch?v=sG0zAn0dL2I", 
                        10, 
                        "Containing 4 minutes of legenedary epicness, it will get you **pumped**!")
        addSong(*default_song)
    print("loading", loadSongs())

    try:
        Bot.run(load_token())
    except aiohttp.client_exceptions.ClientConnectorError as e:
        print(f"connection error running bot: \n\t{e}")
