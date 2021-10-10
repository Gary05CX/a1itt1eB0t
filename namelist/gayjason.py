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
        itchannel = [889535320301924384, 890148548119781396, 894357272141123594, 94358636405604352, 894359609010188288, 894360315356123186, 894361285024686130]
        if msg.content in jasongay :
            if msg.channel.id in itchannel: 
                await msg.channel.send('<@!497380617810608143>')
            
def setup(bot):
    bot.add_cog(jason(bot))