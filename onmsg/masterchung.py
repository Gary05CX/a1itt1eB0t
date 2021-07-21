import discord
from discord.ext import commands
from core.classes import Cog_Extension


class react(Cog_Extension):

    @commands.Cog.listener()
    async def on_message(self, msg):
        id = [576372439940988929]
        if msg.author.id in id:
            await msg.add_reaction("<:chung:867431407554134096> ")

def setup(bot):
    bot.add_cog(react(bot))