import discord
import os, json # default module
from dotenv import load_dotenv

with open('version.json', mode='r',encoding='utf8') as v:
    version = json.load(v)

load_dotenv() # load all the variables from the env file
bot = discord.Bot()

@bot.event
async def on_ready():
    print(f"{bot.user} is ready and online!\nCurrent Version: ", version['version'])

@bot.slash_command(name = "hello", description = "Say hello to the bot")
async def hello(ctx):
    await ctx.respond("Hey!")

bot.run(os.getenv('TOKEN')) # run the bot with the token