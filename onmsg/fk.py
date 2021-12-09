import discord
from discord.ext import commands
from core.classes import Cog_Extension
import time as t

class Onmsg2(Cog_Extension):

    @commands.Cog.listener()
    async def on_message(self, msg):
        if msg.content.endswith('fuck'):
            id = str(msg.author.id)
            local = t.localtime()
            time = t.strftime("%Y %m %d %H:%M:%S", local)
            cmd = str("fuck")
            await msg.channel.send('yourself')
            with open("C:\Discord Bot\Project_1\\a1itt1eB0t\\note.txt", mode="a", encoding="utf-8") as file:
                file.write("\n")
                file.write("\n")
                file.write(time)
                file.write("\n")
                file.write(id)
                file.write("\n")
                file.write(cmd)

def setup(bot):
    bot.add_cog(Onmsg2(bot))