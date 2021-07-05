import discord
from discord.ext import commands
from core.classes import Cog_Extension

class Cmd(Cog_Extension):
    @commands.command()
    async def patgay(self, ctx):
        await ctx.send("<@!491136530254135316> is GAY")

    @commands.command()
    async def morningstar(self, ctx):
        await ctx.send("<@!628223595772116993> is Gay")

def setup(bot):
    bot.add_cog(Cmd(bot))