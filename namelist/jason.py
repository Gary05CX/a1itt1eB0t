import discord
from discord.ext import commands
from core.classes import Cog_Extension
import json

with open('C:\\Discord Bot\\Project_1\\a1itt1eB0t\\setting.json','r',encoding='utf8') as jfile:
    jdata = json.load(jfile)

class jason(Cog_Extension):
    
    @commands.Cog.listener()
    async def on_message(self, msg):
        jasongay = ["張宬碩"]
        if msg.content in jasongay :
            if msg.channel.id == int(jdata['itchannel']): 
                await msg.channel.send('<@!497380617810608143>')
            
def setup(bot):
    bot.add_cog(jason(bot))