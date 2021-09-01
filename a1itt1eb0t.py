import os
import discord
from discord.ext import commands
import json
import random
from discord.ext.commands import Bot

with open('C:\\Discord Bot\\Project_1\\a1itt1eB0t\\setting.json','r',encoding='utf8') as jfile:
    jdata = json.load(jfile)

intents = discord.Intents.all()

bot = commands.Bot(command_prefix='?',intents=intents)

@bot.event
async def on_ready():
    print("on_ready")
    channel = bot.get_channel(int(jdata['A1itt1eB0t']))
    await channel.send("a1itt1eB0t just wake up!!!")

for filename in os.listdir('C:\\Discord Bot\\Project_1\\a1itt1eB0t\\cmds'):
    if filename.endswith('.py'):
        bot.load_extension(f'cmds.{filename[:-3]}')

for filename in os.listdir('C:\\Discord Bot\\Project_1\\a1itt1eB0t\\onmsg'):
    if filename.endswith('.py'):
        bot.load_extension(f'onmsg.{filename[:-3]}')

for filename in os.listdir('C:\\Discord Bot\\Project_1\\a1itt1eB0t\\timetable'):
    if filename.endswith('.py'):
        bot.load_extension(f'timetable.{filename[:-3]}')

if __name__ == "__main__":
    bot.run(jdata['TOKEN'])