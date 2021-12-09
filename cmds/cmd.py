import discord
from discord.ext import commands
from core.classes import Cog_Extension
import time as t

class Cmd(Cog_Extension):
    @commands.command()
    async def patgay(self, ctx):
        id = str(ctx.author.id)
        local = t.localtime()
        time = t.strftime("%Y %m %d %H:%M:%S", local)
        cmd = str("patgay")
        await ctx.send("<@!491136530254135316> is GAY")
        with open("C:\Discord Bot\Project_1\\a1itt1eB0t\\note.txt", mode="a", encoding="utf-8") as file:
            file.write("\n")
            file.write("\n")
            file.write(time)
            file.write("\n")
            file.write(id)
            file.write("\n")
            file.write(cmd)

    @commands.command()
    async def morningstar(self, ctx):
        id = str(ctx.author.id)
        local = t.localtime()
        time = t.strftime("%Y %m %d %H:%M:%S", local)
        cmd = str("moringstar")
        await ctx.send("<@!628223595772116993> is Gay")
        with open("C:\Discord Bot\Project_1\\a1itt1eB0t\\note.txt", mode="a", encoding="utf-8") as file:
            file.write("\n")
            file.write("\n")
            file.write(time)
            file.write("\n")
            file.write(id)
            file.write("\n")
            file.write(cmd)
    
    @commands.command()
    async def shitsam(self, ctx):
        id = str(ctx.author.id)
        local = t.localtime()
        time = t.strftime("%Y %m %d %H:%M:%S", local)
        cmd = str("shitsam")
        await ctx.send("<@!628223595772116993> eat shit la!!!")
        with open("C:\Discord Bot\Project_1\\a1itt1eB0t\\note.txt", mode="a", encoding="utf-8") as file:
            file.write("\n")
            file.write("\n")
            file.write(time)
            file.write("\n")
            file.write(id)
            file.write("\n")
            file.write(cmd)
    

def setup(bot):
    bot.add_cog(Cmd(bot))