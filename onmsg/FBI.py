import discord
from discord.ext import commands
from core.classes import Cog_Extension

class FBI(Cog_Extension):

    @commands.Cog.listener()
    async def on_message(self, msg):
        loli = ["loli", "ロリ", "蘿莉", "蘿莉控", "LOLI", "Loli", "小蘿莉"]
        if msg.content in loli:
            await msg.channel.send('FBI open up!!!!!')

def setup(bot):
    bot.add_cog(FBI(bot))