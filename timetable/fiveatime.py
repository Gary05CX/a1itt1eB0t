import discord
from discord.ext import commands
from core.classes import Cog_Extension

class Atime(Cog_Extension):
    @commands.command()
    async def amon(self, ctx):
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

    @commands.command()
    async def atue(self, ctx):
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

    @commands.command()
    async def awed(self, ctx):
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

    @commands.command()
    async def athu(self, ctx):
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

    @commands.command()
    async def afri(self, ctx):
        await ctx.send("""Arrived
LS
LS

1X
1X
?

MATH
MATH

""")

def setup(bot):
    bot.add_cog(Atime(bot))