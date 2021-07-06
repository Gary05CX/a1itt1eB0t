import discord
from discord.ext import commands
from core.classes import Cog_Extension

class Onmsg3(Cog_Extension):

    @commands.Cog.listener()
    async def on_message(self, msg):
        if msg.content == 'あくあ':
            await msg.channel.send(' <@!626419302232227841> 的老婆 ')

def setup(bot):
    bot.add_cog(Onmsg3(bot))