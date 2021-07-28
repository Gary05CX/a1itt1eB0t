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
        2021-07-25          1500
        2021-07-26          1900
        2021-07-27          1600
        2021-07-28          1600
        2021-07-29          1900
        XXXX-XX-XX          XXXX
        """)
        print("sameone asked gary")

def setup(bot):
    bot.add_cog(Main(bot))