import discord
from discord.ext import commands
from core.classes import Cog_Extension
import time as t

class Atime(Cog_Extension):
    @commands.command()
    async def amon(self, ctx):
        id = str(ctx.author.id)
        local = t.localtime()
        time = t.strftime("%Y %m %d %H:%M:%S", local)
        cmd = str("amon")
        await ctx.send("""Arrived
ENG
ENG

CHI 
PE
PE

CHI
2X
2X
""")
        with open("C:\Discord Bot\Project_1\\a1itt1eB0t\\note.txt", mode="a", encoding="utf-8") as file:
            file.write("\n")
            file.write("\n")
            file.write(time)
            file.write("\n")
            file.write(id)
            file.write("\n")
            file.write(cmd)

    @commands.command()
    async def atue(self, ctx):
        id = str(ctx.author.id)
        local = t.localtime()
        time = t.strftime("%Y %m %d %H:%M:%S", local)
        cmd = str("atue")
        await ctx.send("""Arrived
1X
1X

MATH
ART
ART

2X
ENG
ENG
""")
        with open("C:\Discord Bot\Project_1\\a1itt1eB0t\\note.txt", mode="a", encoding="utf-8") as file:
            file.write("\n")
            file.write("\n")
            file.write(time)
            file.write("\n")
            file.write(id)
            file.write("\n")
            file.write(cmd)

    @commands.command()
    async def awed(self, ctx):
        id = str(ctx.author.id)
        local = t.localtime()
        time = t.strftime("%Y %m %d %H:%M:%S", local)
        cmd = str("awed")
        await ctx.send("""Arrived
CHI
CHI

LS
2X
2X

MATH
ENG
ENG
""")
        with open("C:\Discord Bot\Project_1\\a1itt1eB0t\\note.txt", mode="a", encoding="utf-8") as file:
            file.write("\n")
            file.write("\n")
            file.write(time)
            file.write("\n")
            file.write(id)
            file.write("\n")
            file.write(cmd)

    @commands.command()
    async def athu(self, ctx):
        id = str(ctx.author.id)
        local = t.localtime()
        time = t.strftime("%Y %m %d %H:%M:%S", local)
        cmd = str("athu")
        await ctx.send("""Arrived
MATH
MATH

LS
LS
1X

CHI
CHI
ENG
""")
        with open("C:\Discord Bot\Project_1\\a1itt1eB0t\\note.txt", mode="a", encoding="utf-8") as file:
            file.write("\n")
            file.write("\n")
            file.write(time)
            file.write("\n")
            file.write(id)
            file.write("\n")
            file.write(cmd)

    @commands.command()
    async def afri(self, ctx):
        id = str(ctx.author.id)
        local = t.localtime()
        time = t.strftime("%Y %m %d %H:%M:%S", local)
        cmd = str("afri")
        await ctx.send("""Arrived
LS
LS

1X
1X
?

MATH
MATH

""")
        with open("C:\Discord Bot\Project_1\\a1itt1eB0t\\note.txt", mode="a", encoding="utf-8") as file:
            file.write("\n")
            file.write("\n")
            file.write(time)
            file.write("\n")
            file.write(id)
            file.write("\n")
            file.write(cmd)

def setup(bot):
    bot.add_cog(Atime(bot))