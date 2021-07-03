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
    print(">> a1itt1ebot is online!!! <<")
    channel = bot.get_channel(int(jdata['A1itt1eB0t']))
    await channel.send("a1itt1eB0t is online!!")

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

@bot.command()
async def ping(ctx):
    await ctx.send(f"{round(bot.latency*1000)} ms")
    print(bot.latency)

@bot.command()
async def patgay(ctx):
    await ctx.send("(@patfat#4559) is GAY")

@bot.command()
async def morningstar(ctx):
    await ctx.send("Sam is Gay")

@bot.command()
async def sampic(ctx):
    random_pic = random.choice(jdata['sam'])
    pic = discord.File(random_pic)
    await ctx.send(file= pic)
    
bot.run(jdata['TOKEN'])