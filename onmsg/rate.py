import discord
from discord.ext import commands
from core.classes import Cog_Extension
from random import randrange
import time as t

class rate(Cog_Extension):

    @commands.Cog.listener()
    async def on_message(self, msg):
        RATE = ("rate","機率", "勝率", "敗率")
        a = randrange(100) + 1
        b = randrange(100) + 1
        c = a+b
        list = [a, b, c]
        id = str(msg.author.id)
        local = t.localtime()
        time = t.strftime("%Y %m %d %H:%M:%S", local)
        cmd = str("rate")
        if msg.content.endswith(RATE) or msg.content in RATE :
            with open("C:\Discord Bot\Project_1\\a1itt1eB0t\\note.txt", mode="a", encoding="utf-8") as file:
                file.write("\n")
                file.write("\n")
                file.write(time)
                file.write("\n")
                file.write(id)
                file.write("\n")
                file.write(cmd)
            possive = ["<@!626419302232227841>", "<@!723473163341791314>"]
            negative = ["gay", "ばか", "白痴", "on9", "6uo"]
            if msg.content in negative:
                passid = [626419302232227841, 723473163341791314, 673142050597765140]
                if msg.author.id not in passid:
                    if a >= b:
                        if a >= 50:
                            await msg.channel.send(str(a) + "%")
                            print(str(a) + "%")
                            print(list)
                        elif a < 50:
                            await msg.channel.send(str(a) + "%")
                            print(str(a) + "%")
                            print(list)
                    if b > a:
                        if b >= 50:
                            await msg.channel.send(str(b) + "%")
                            print(str(b) + "%")
                            print(list)
                        elif b < 50:
                            await msg.channel.send(str(b) + "%")
                            print(str(b) + "%")
                            print(list)
                elif msg.author.id in passid:
                    if a <= b:
                        if a >= 50:
                            await msg.channel.send(str(a) + "%")
                            print(str(a) + "%")
                            print(list)
                        elif a < 50:
                            await msg.channel.send(str(a) + "%")
                            print(str(a) + "%")
                            print(list)
                    if b < a:
                        if b >= 50:
                            await msg.channel.send(str(b) + "%")
                            print(str(b) + "%")
                            print(list)
                        elif b < 50:
                            await msg.channel.send(str(b) + "%")
                            print(str(b) + "%")
                            print(list)
            else:
                if b >= 50:
                    await msg.channel.send(str(b) + "%")
                    print(str(b) + "%")
                    print(list)
                elif b < 50:
                    await msg.channel.send(str(b) + "%")
                    print(str(b) + "%")
                    print(list)
def setup(bot):
    bot.add_cog(rate(bot))