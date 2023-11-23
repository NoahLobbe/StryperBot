import os
import discord
import discord.ext.commands
import validators
import json


###
def isValidYoutubeURL(url):
    return bool(validators.url(url))




###Bot stuff

BOT_TOKEN = os.getenv('STRYPER_BOT_TOKEN') 
assert BOT_TOKEN is not None

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
async def add(ctx, url:str, rating:int):
    print(type(url), url)
    if isValidYoutubeURL(url):
        msg = f"Adding '{url}' with rating {rating}/10"
    else:
        msg = f"'{url}' is not reachable"
        
    print(msg)
    await ctx.send(msg)
        

    
if __name__ == "__main__":
    Bot.run(BOT_TOKEN)
