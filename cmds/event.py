import discord
from discord.ext import commands
from core.classes import Cog_Extension
import random 
import json

with open('setting.json','r',encoding='utf8') as jfile:
        jdata = json.load(jfile)

class Event(Cog_Extension):
    @commands.Cog.listener()
    async def on_member_join(self, member):
        print(f"{member} join!")
        channel = self.bot.get_channel(int(jdata['A1itt1eB0t']))
        await channel.send(f"{member} join!")

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        print(f"{member} leave!")
        channel = self.bot.get_channel(int(jdata['A1itt1eB0t']))
        await channel.send(f"{member} leave!")

def setup(bot):
    bot.add_cog(Event(bot))