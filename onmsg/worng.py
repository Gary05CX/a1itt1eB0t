import discord
from discord.ext import commands
from core.classes import Cog_Extension

class wrong(Cog_Extension):

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.errors.MissingRequiredArgument):
            await ctx.send("Missing required argument 遺失參數!!")
        elif isinstance(error, commands.errors.CommandNotFound):
             await ctx.send("Commands not found  沒這指令!!")
<<<<<<< HEAD
        else:
            await ctx.send("something goes wrong  發生錯誤!!!")
=======
        alse:
            await ctx.send("wrong")
>>>>>>> 135fdc61c3cb04828778a3373addd417028bcd75

def setup(bot):
    bot.add_cog(wrong(bot))
