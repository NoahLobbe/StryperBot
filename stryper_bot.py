#standard python libraries
import os
import json

#denpendencies
import discord
import discord.ext.commands
import validators
from dotenv import load_dotenv


###
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
    Bot.run(load_token())
