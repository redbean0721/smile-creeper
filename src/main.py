import discord
import os, json, yaml # default module
from dotenv import load_dotenv

with open('config.yml', 'r') as setting:
    config = yaml.safe_load(setting)

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

@bot.slash_command(description = "載入Cog (限擁有者)")
async def load(ctx, extension):
    if ctx.author.id == int(config['BotOwnerConfig']['owner_id']):
        print(f'Loading {extension} ...')
        bot.load_extension(f'cmds.{extension}')
        await ctx.respond(f'Loaded {extension} done.')
    else:
        await ctx.respond(f"{ctx.author.mention} 你沒有權限")

@bot.slash_command(description = "卸載Cog (限擁有者)")
async def unload(ctx, extension):
    if ctx.author.id == int(config['BotOwnerConfig']['owner_id']):
        print(f'Un - Loading {extension} ...')
        bot.unload_extension(f'cmds.{extension}')
        await ctx.respond(f'Un - Loaded {extension} done.')
    else:
        await ctx.respond(f"{ctx.author.mention} 你沒有權限")

@bot.slash_command(description = "重新載入Cog (限擁有者)")
async def reload(ctx, extension):
    if ctx.author.id == int(config['BotOwnerConfig']['owner_id']):
        print(f'RE - Loading {extension} ...')
        bot.reload_extension(f'cmds.{extension}')
        await ctx.respond(f'RE - Loaded {extension} done.')
    else:
        await ctx.respond(f"{ctx.author.mention} 你沒有權限")

for filename in os.listdir('./src/cmds'):
    if filename.endswith('.py'):
        bot.load_extension(f'cmds.{filename[:-3]}')

if __name__ == '__main__': 
    bot.run(os.getenv('TOKEN')) # run the bot with the token