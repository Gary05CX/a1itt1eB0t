import discord
from discord.ext import commands
from core.classes import Cog_Extension

class Onmsg2(Cog_Extension):

    @commands.Cog.listener()
    async def on_message(self, msg):
        if msg.content.endswith('fuck'):
            await msg.channel.send('yourself')

def setup(bot):
    bot.add_cog(Onmsg2(bot))