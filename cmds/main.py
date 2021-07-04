import discord
from discord.ext import commands
from core.classes import Cog_Extension

class Main(Cog_Extension):

    @commands.command()
    async def ping(self, ctx):
        await ctx.send('f{round(self.bot.latency*1000)} ms')

    @commands.command()
    async def gary(self, ctx):
        await ctx.send("[2021-07-04-->1015:go out;(maybe)1500:back home and free];\
        [2021-07-05-->0800:go out;(maybe)1500:back home and free];\
        [2021-07-06-->0800:go out;(maybe)1500:back home and free]")
        print("sameone ask gary")

def setup(bot):
    bot.add_cog(Main(bot))