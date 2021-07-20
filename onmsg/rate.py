import discord
from discord.ext import commands
from core.classes import Cog_Extension
from random import randrange

class rate(Cog_Extension):

    @commands.Cog.listener()
    async def on_message(self, msg):
        RATE = ("rate","機率")
        a = randrange(100) + 1
        b = randrange(100) + 1
        c = a+b
        list = [a, b, c]
        if msg.content.endswith(RATE) :
            possive = ["<@!626419302232227841>", "<@!723473163341791314>"]
            negative = ["gay", "ばか", "白痴", "on9", "6uo"]
            if msg.content in negative:
                passid = [626419302232227841, 723473163341791314, 673142050597765140]
                if msg.author.id not in passid:
                    if a >= b:
                        if a >= 50:
                            await msg.channel.send("YES," + str(a) + "%")
                            print(str(a) + "%")
                            print(list)
                        elif a < 50:
                            await msg.channel.send("NO," + str(a) + "%")
                            print(str(a) + "%")
                            print(list)
                    if b > a:
                        if b >= 50:
                            await msg.channel.send("YES," + str(b) + "%")
                            print(str(b) + "%")
                            print(list)
                        elif b < 50:
                            await msg.channel.send("NO," + str(b) + "%")
                            print(str(b) + "%")
                            print(list)
                elif msg.author.id in passid:
                    if a <= b:
                        if a >= 50:
                            await msg.channel.send("YES," + str(a) + "%")
                            print(str(a) + "%")
                            print(list)
                        elif a < 50:
                            await msg.channel.send("NO," + str(a) + "%")
                            print(str(a) + "%")
                            print(list)
                    if b < a:
                        if b >= 50:
                            await msg.channel.send("YES," + str(b) + "%")
                            print(str(b) + "%")
                            print(list)
                        elif b < 50:
                            await msg.channel.send("NO," + str(b) + "%")
                            print(str(b) + "%")
                            print(list)
            else:
                if b >= 50:
                    await msg.channel.send("YES," + str(b) + "%")
                    print(str(b) + "%")
                    print(list)
                elif b < 50:
                    await msg.channel.send("NO," + str(b) + "%")
                    print(str(b) + "%")
                    print(list)
def setup(bot):
    bot.add_cog(rate(bot))