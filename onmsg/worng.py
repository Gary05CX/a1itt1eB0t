import discord
from discord.ext import commands
from core.classes import Cog_Extension

class wrong(Cog_Extension):

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.errors.MissingRequiredArgument):
            await ctx.send("MissingRequiredArgument!!")
        elif isinstance(error, commands.errors.CommandNotFound):
             await ctx.send("Commands not found  沒這指令!!")
        alse:
            await ctx.send("wrong")

def setup(bot):
    bot.add_cog(wrong(bot))
