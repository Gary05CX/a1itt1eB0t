import discord
from discord.ext import commands
from core.classes import Cog_Extension
from random import randrange
import json

with open('C:\\Discord Bot\\Project_1\\a1itt1eB0t\\setting.json','r',encoding='utf8') as jfile:
    jdata = json.load(jfile)

class gary(Cog_Extension):
    
    @commands.Cog.listener()
    async def on_message(self, msg):
        akukingary = ["gary", "<@!626419302232227841>", "<@!723473163341791314>", "<@!883577132318593074>"]
        itchannel = [889535320301924384, 890148548119781396, 894357272141123594, 94358636405604352, 894359609010188288, 894360315356123186, 894361285024686130]

        if msg.content in akukingary :
            if msg.channel.id in itchannel: 
                await msg.channel.send('<@&889534342370582589>')
            else:
                x = randrange(2)
                if x == 0:
                    await msg.channel.send("<@&870164299589484644>")
                elif x == 1:
                    await msg.channel.send("<@&676135324266790913>")
                    
def setup(bot):
    bot.add_cog(gary(bot))