import discord
from discord.ext import commands
from core.classes import Cog_Extension

class Onmsg(Cog_Extension):
    @commands.Cog.listener()
    async def on_message(self, msg):
        if msg.content == 'ばか' and msg.author.id == "626419302232227841" :
            await msg.channel.send('は？')        

def setup(bot):
    bot.add_cog(Onmsg(bot))