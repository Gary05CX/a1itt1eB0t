import discord
from discord.ext import commands
from core.classes import Cog_Extension
import time as t

class everyoneban(Cog_Extension):

    @commands.Cog.listener()
    async def on_message(self, msg):
        if msg.content == 'あくあ':
            id = str(msg.author.id)
            local = t.localtime()
            time = t.strftime("%Y %m %d %H:%M:%S", local)
            cmd = str("everyoneban")
            everyone = ["<@!924157725674442783>", "@everyone"]
            gary = [626419302232227841,723473163341791314,883577132318593074]
            if msg.content in everyone and msg.author.id != gary:
                await msg.channel.send("""
            pls dont using ```
            @everyone
            ```""")
            with open("C:\Discord Bot\Project_1\\a1itt1eB0t\\note.txt", mode="a", encoding="utf-8") as file:
                file.write("\n")
                file.write("\n")
                file.write(time)
                file.write("\n")
                file.write(id)
                file.write("\n")
                file.write(cmd)

def setup(bot):
    bot.add_cog(everyoneban(bot))