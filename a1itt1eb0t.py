import os
import discord
from discord.ext import commands
import json
import random

with open('setting.json','r',encoding='utf8') as jfile:
        jdata = json.load(jfile)

intents = discord.Intents.all()

bot = commands.Bot(command_prefix='?',intents=intents)

@bot.event
async def on_ready():
    print("on_ready")
    channel = bot.get_channel(int(jdata['A1itt1eB0t']))
    await channel.send("a1itt1eB0t just wake up!!!")

@bot.event
async def on_member_join(member):
    print(f"{member} join!")
    channel = bot.get_channel(int(jdata['A1itt1eB0t']))
    await channel.send(f"{member} join!")

@bot.event
async def on_member_remove(member):
    print(f"{member} leave!")
    channel = bot.get_channel(int(jdata['A1itt1eB0t']))
    await channel.send(f"{member} leave!")

for filename in os.listdir('./cmds'):
    if filename.endswith('.py'):
        bot.load_extension(f'cmds.{filename[:-3]}')

if __name__ == "__main__":
    bot.run(jdata['TOKEN'])
