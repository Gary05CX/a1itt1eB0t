import discord
from discord.ext import commands
from core.classes import Cog_Extension

class Onmsg(Cog_Extension):
    @commands.Cog.listener()
    async def on_message(self, msg):
        if msg.content == 'ばか' and msg.author.id == 626419302232227841 or msg.author.id == 723473163341791314 :
            await msg.channel.send('は？')

    @commands.Cog.listener()
    async def on_message(self, msg):
        if msg.content.endswith('fuck') :
            await msg.channel.send('yourself')        
 
    @commands.Cog.listener()
    async def on_message(self, msg):
        if msg.content == 'あくあ':
            await msg.channel.send(' <@!626419302232227841> 的老婆 ')


def setup(bot):
    bot.add_cog(Onmsg(bot))