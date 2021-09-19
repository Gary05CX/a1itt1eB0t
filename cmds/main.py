import discord
from discord.ext import commands
from core.classes import Cog_Extension

class Main(Cog_Extension):

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'{round(self.bot.latency*1000)} ms')

    @commands.command()
    async def gary(self, ctx):
        await ctx.send("1600(Mon,Tue,Wed,Fri);1600-1700&2000(Thu);1900(Sat);1500(Sun)")
        print("sameone asked gary")

def setup(bot):
    bot.add_cog(Main(bot))