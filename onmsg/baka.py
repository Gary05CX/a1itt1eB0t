import discord
from discord.ext import commands
from core.classes import Cog_Extension

class Onmsg1(Cog_Extension):
    
    @commands.Cog.listener()
    async def on_message(self, msg):
        if msg.content == 'ばか' and msg.author.id == 626419302232227841 or msg.author.id == 723473163341791314 :
            await msg.channel.send('は？')

def setup(bot):
    bot.add_cog(Onmsg1(bot))