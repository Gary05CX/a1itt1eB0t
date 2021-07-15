import discord
from discord.ext import commands
from core.classes import Cog_Extension
from random import randrange

class rate(Cog_Extension):

    @commands.Cog.listener()
    async def on_message(self, msg):
        if msg.content.endswith("rate") or msg.content.endswith("機率"):
            a = randrange(100)
            await msg.channel.send(str(a)+"%")

def setup(bot):
    bot.add_cog(rate(bot))