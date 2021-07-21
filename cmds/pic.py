import discord
from discord.ext import commands
from core.classes import Cog_Extension
import random 
import json

with open('C:\\Discord Bot\\Project_1\\a1itt1eB0t\\setting.json','r',encoding='utf8') as jfile:
        jdata = json.load(jfile)

class Pic(Cog_Extension):
    @commands.command()
    async def sampic(self, ctx):
        random_pic = random.choice(jdata['sam'])
        pic = discord.File(random_pic)
        await ctx.send(file= pic)

    @commands.command()
    async def patpic(self, ctx):
        random_pic = random.choice(jdata['patgay'])
        pic = discord.File(random_pic)
        await ctx.send(file= pic)

    @commands.command()
    async def chung(self, ctx):
        pic = discord.File('C:\\Discord Bot\\Project_1\\a1itt1eB0t\\masterchung\\IMG-20210417-WA0027.jpg')
        await ctx.send(file= pic)

def setup(bot):
    bot.add_cog(Pic(bot))