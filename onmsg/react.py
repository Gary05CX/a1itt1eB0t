import discord
from discord.ext import commands
from core.classes import Cog_Extension
import json
import time as t

with open('C:\\Discord Bot\\Project_1\\a1itt1eB0t\\setting.json','r',encoding='utf8') as jfile:
    jdata = json.load(jfile)

class react(Cog_Extension):

    @commands.Cog.listener()
    async def on_message(self, msg):
        wife = ["老婆", "my wife"]
        id = [626419302232227841, 723473163341791314]
        if msg.content in wife:
            if msg.author.id not in id:
                id = str(msg.author.id)
                local = t.localtime()
                time = t.strftime("%Y %m %d %H:%M:%S", local)
                cmd = str("wakeup")
                await msg.add_reaction("<:wake_up:831196189407576134>")
                with open("C:\Discord Bot\Project_1\\a1itt1eB0t\\note.txt", mode="a", encoding="utf-8") as file:
                    file.write("\n")
                    file.write("\n")
                    file.write(time)
                    file.write("\n")
                    file.write(id)
                    file.write("\n")
                    file.write(cmd)

def setup(bot):
    bot.add_cog(react(bot))