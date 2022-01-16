import discord
from discord.ext import commands
from core.classes import Cog_Extension
import random 
import json
import time as t

with open('C:\\Discord Bot\\Project_1\\a1itt1eB0t\\setting.json','r',encoding='utf8') as jfile:
    jdata = json.load(jfile)

class timer(Cog_Extension):
    @commands.command()
    async def warframetimer(self, ctx, mun:int, round:int, unit:str):
        id = str(ctx.author.id)
        local = t.localtime()
        time = t.strftime("%Y %m %d %H:%M:%S", local)
        cmd = str("warframetimer")
        with open("C:\Discord Bot\Project_1\\a1itt1eB0t\\note.txt", mode="a", encoding="utf-8") as file:
            file.write("\n")
            file.write("\n")
            file.write(time)
            file.write("\n")
            file.write(id)
            file.write("\n")
            file.write(cmd)
        def unitcheck(unit):
            if unit == "s" :
                timer = mun
                return timer 
            elif unit == "m":
                timer = mun*60
                return timer
            else:
                timer = mun
                return timer
        def ncheck(unit):
            if unit == "s" or "m" :
                n = 0
                return n
            elif unit == "stop" :
                n = round
                return round
        timer = unitcheck(str(unit))
        n = ncheck(str(unit))
        while n < round:
            t.sleep(int(timer))
            n += 1 
            channel = self.bot.get_channel(926342317567250452)
            await channel.send("<@!"+id+">"+ "time up!!!"+"("+str(n)+"/"+str(round)+")")
            await channel.send("```"+"\n"+time+"```")
            with open("C:\Discord Bot\Project_1\\a1itt1eB0t\\note.txt", mode="a", encoding="utf-8") as file:
                file.write("\n")
                file.write("\n")
                file.write(time)
                file.write("\n")
                file.write(id)
                file.write("\n")
                file.write("warframetimer")
                file.write("("+str(n)+"/"+str(round)+")")
        
    @commands.command()
    async def timerhelp(self, ctx):
        id = str(ctx.author.id)
        local = t.localtime()
        time = t.strftime("%Y %m %d %H:%M:%S", local)
        cmd = str("timerhelp")
        with open("C:\Discord Bot\Project_1\\a1itt1eB0t\\note.txt", mode="a", encoding="utf-8") as file:
            file.write("\n")
            file.write("\n")
            file.write(time)
            file.write("\n")
            file.write(id)
            file.write("\n")
            file.write(cmd)
        await ctx.send("""```
?warframetimer (time) (round) (unit:s/m)
CANNOT stop!!!!!!!!!!!```""")

def setup(bot):
    bot.add_cog(timer(bot))