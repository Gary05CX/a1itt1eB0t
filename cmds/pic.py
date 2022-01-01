import discord
from discord.ext import commands
from core.classes import Cog_Extension
import random 
import json
import time as t

with open('C:\\Discord Bot\\Project_1\\a1itt1eB0t\\setting.json','r',encoding='utf8') as jfile:
    jdata = json.load(jfile)

class Pic(Cog_Extension):
    @commands.command()
    async def sampic(self, ctx):
        id = str(ctx.author.id)
        local = t.localtime()
        time = t.strftime("%Y %m %d %H:%M:%S", local)
        cmd = str("sampic")
        random_pic = random.choice(jdata['sam'])
        pic = discord.File(random_pic)
        await ctx.send(file= pic)
        with open("C:\Discord Bot\Project_1\\a1itt1eB0t\\note.txt", mode="a", encoding="utf-8") as file:
            file.write("\n")
            file.write("\n")
            file.write(time)
            file.write("\n")
            file.write(id)
            file.write("\n")
            file.write(cmd)

    @commands.command()
    async def patpic(self, ctx):
        id = str(ctx.author.id)
        local = t.localtime()
        time = t.strftime("%Y %m %d %H:%M:%S", local)
        cmd = str("patpic")
        random_pic = random.choice(jdata['patgay'])
        pic = discord.File(random_pic)
        await ctx.send(file= pic)
        with open("C:\Discord Bot\Project_1\\a1itt1eB0t\\note.txt", mode="a", encoding="utf-8") as file:
            file.write("\n")
            file.write("\n")
            file.write(time)
            file.write("\n")
            file.write(id)
            file.write("\n")
            file.write(cmd)

    @commands.command()
    async def jasonpic(self, ctx):
        id = str(ctx.author.id)
        local = t.localtime()
        time = t.strftime("%Y %m %d %H:%M:%S", local)
        cmd = str("jasonpic")
        random_pic = random.choice(jdata['jason'])
        pic = discord.File(random_pic)
        await ctx.send(file= pic)
        with open("C:\Discord Bot\Project_1\\a1itt1eB0t\\note.txt", mode="a", encoding="utf-8") as file:
            file.write("\n")
            file.write("\n")
            file.write(time)
            file.write("\n")
            file.write(id)
            file.write("\n")
            file.write(cmd)

    @commands.command()
    async def chung(self, ctx):
        id = str(ctx.author.id)
        local = t.localtime()
        time = t.strftime("%Y %m %d %H:%M:%S", local)
        cmd = str("chung")
        pic = discord.File('C:\\Discord Bot\\Project_1\\a1itt1eB0t\\masterchung\\IMG-20210417-WA0027.jpg')
        await ctx.send("<@!576372439940988929>")
        await ctx.send(file= pic)
        with open("C:\Discord Bot\Project_1\\a1itt1eB0t\\note.txt", mode="a", encoding="utf-8") as file:
            file.write("\n")
            file.write("\n")
            file.write(time)
            file.write("\n")
            file.write(id)
            file.write("\n")
            file.write(cmd)


def setup(bot):
    bot.add_cog(Pic(bot))