#standard python libraries
import os
import json
import random as rand

#denpendencies
import discord
import discord.ext.commands
import validators
from dotenv import load_dotenv

###Constants
JSON_INDENTS = 4
SONGS_FILE = "songs.json"


### Setup functions
def checkSongsFile():
    """Returns True if already existed, and False if file had to be made"""
    if not os.path.exists(SONGS_FILE):
        print(f"Making '{SONGS_FILE}'")
        with open(SONGS_FILE, "w+") as new_file:
            data = {"songs": []}
            json.dump(data, new_file, indent=JSON_INDENTS)
        return False
    return True


### Functions for Bot
def validateYoutubeURL(url):
    is_valid_url = bool(validators.url(url))
    if is_valid_url:
        return True
        '''
        YT_Obj = pytube.YouTube(url)
        print(YT_Obj,YT_Obj.channel_id,YT_Obj.channel_url)
        if YT_Obj.author == "The Official Stryper Channel":
            #eventually add a function for certain people to override
            #if it is actually a stryper song
            return True 
        else:
            return False
        '''
                
    else:
        return False

def validateRating(rating_str):
    if rating_str.isdigit():
        rating = int(rating_str)
        return (rating >= 0 and rating <= 10)
    else:
        return False


##songs JSON stuff
def songMessage(song_dict):
    intro = "***Hello everybody and WELCOME to Stryper Saturday!!!***" 
    description = f"\nToday is the amazing song *{song_dict['title']}*, with a rating of {song_dict['rating']}/10: "
    link = song_dict["url"]
    notes = song_dict["notes"]
    return intro + description + link, notes


def loadSongs():
    with open(SONGS_FILE, "r") as read_file:
        return json.load(read_file)
    
    
def addSong(title, url, rating, notes):
    new_data = {"title":title, "url":url, "rating":rating, "notes":notes}
    current_data_json = loadSongs()

    with open(SONGS_FILE, "w") as write_file:
        current_data_json["songs"].append(new_data) #updated

        json.dump(current_data_json, write_file, indent=JSON_INDENTS)


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

@Bot.event
async def on_ready():
    print(f"{Bot.user} has connected to Discord!")

@Bot.command()
async def greet(ctx):
    await Bot.change_presence(status=discord.Status.online)
    
    print("sending greeting...")
    await ctx.send("Hello there!")

    await Bot.change_presence(status=discord.Status.offline)

@Bot.command()
async def random(ctx):
    song = _getRandomSong()
    msg, note = songMessage(song)
    await ctx.send(msg)
    await ctx.send(note)

@Bot.command()
async def add(ctx, *arguements):
    #parse user input
    print(f"User inputted: {arguements}")
    youtube_url = arguements[0]
    rating = arguements[1]
    

    #validate user input
    url_is_legit = validateYoutubeURL(youtube_url)
    rating_is_legit = validateRating(rating)

    url_invalid_str = f"'{youtube_url}' is not reachable"
    rating_invalid_str = f"'{rating}' is invalid, has to be a positive integer from 0 to 10"
    

    #output stufff
    if url_is_legit and rating_is_legit:
        msg = f"Adding '{youtube_url}' with rating {rating}/10"
        
    elif url_is_legit and not rating_is_legit:
        msg = rating_invalid_str

    elif not url_is_legit and rating_is_legit:
        msg = url_invalid_str

    else:
        msg = url_invalid_str + ", and " + rating_invalid_str
        
    print(msg)
    await ctx.send(msg)
        

    
if __name__ == "__main__":
    already_existed = checkSongsFile()
    if not already_existed:
        default_song = ("To Hell with the Devil", 
                        "https://www.youtube.com/watch?v=sG0zAn0dL2I", 
                        10, 
                        "Containing 4 minutes of legenedary epicness, it will get you **pumped**!")
        addSong(*default_song)
    print("loading", loadSongs())
    Bot.run(load_token())
