import discord
from discord.ext import commands
from core.classes import Cog_Extension
import time as t

class FBI(Cog_Extension):

    @commands.Cog.listener()
    async def on_message(self, msg):
        id = str(msg.author.id)
        local = t.localtime()
        time = t.strftime("%Y %m %d %H:%M:%S", local)
        cmd = str("loli")
        loli = ["loli", "ロリ", "蘿莉", "蘿莉控", "LOLI", "Loli", "小蘿莉"]
        if msg.content in loli:
            await msg.channel.send('FBI open up!!!!!')
            with open("C:\Discord Bot\Project_1\\a1itt1eB0t\\note.txt", mode="a", encoding="utf-8") as file:
                file.write("\n")
                file.write("\n")
                file.write(time)
                file.write("\n")
                file.write(id)
                file.write("\n")
                file.write(cmd)

def setup(bot):
    bot.add_cog(FBI(bot))