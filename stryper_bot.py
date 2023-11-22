import os
import discord
import discord.ext.commands

BOT_TOKEN = os.getenv('STRYPER_BOT_TOKEN') 
assert BOT_TOKEN is not None


intents = discord.Intents.default()
print(intents)
intents.message_content = True #enables sending messages?

Bot = discord.ext.commands.Bot(command_prefix=".", intents=intents)

@Bot.event
async def on_ready():
    print(f"{Bot.user} has connected to Discord!")

@Bot.command()
async def greet(ctx):
    await Bot.change_presence(status=discord.Status.online)
    
    print("sending greeting...")
    await ctx.send("Hello there!")

    await Bot.change_presence(status=discord.Status.offline)

Bot.run(BOT_TOKEN)
