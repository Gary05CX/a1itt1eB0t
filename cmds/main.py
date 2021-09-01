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
        2021-08-04          1800
        2021-08-05          1600
        2021-08-06          0000
        2021-08-07          0000
        2021-08-08          0000
        XXXX-XX-XX          XXXX
        """)
        print("sameone asked gary")

def setup(bot):
    bot.add_cog(Main(bot))