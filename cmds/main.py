import discord
from discord.ext import commands
from core.classes import Cog_Extension

class Main(Cog_Extension):

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'{round(self.bot.latency*1000)} ms')

    @commands.command()
    async def gary(self, ctx):
        await ctx.send("""DATE           TIME(Free at)
        2021-07-23          1600
        2021-07-24          2000
        2021-07-25          1500
        XXXX-XX-XX          XXXX
        """)
        print("sameone ask gary")

def setup(bot):
    bot.add_cog(Main(bot))