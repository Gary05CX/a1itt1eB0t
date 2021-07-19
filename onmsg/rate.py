import discord
from discord.ext import commands
from core.classes import Cog_Extension
from random import randrange

class rate(Cog_Extension):

    @commands.Cog.listener()
    async def on_message(self, msg):
        if msg.content.endswith("rate") or msg.content.endswith("機率"):
            a = randrange(100)
            if a > 50:
                await msg.channel.send("是"+","+str(a)+"%")
            elif a < 50:
                await msg.channel.send("否"+","+str(a)+"%")

def setup(bot):
    bot.add_cog(rate(bot))