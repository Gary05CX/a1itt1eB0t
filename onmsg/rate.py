import discord
from discord.ext import commands
from core.classes import Cog_Extension
from random import randrange

class rate(Cog_Extension):

    @commands.Cog.listener()
    async def on_message(self, msg):
        RATE = ["rate","機率"]
        a = randrange(100)
        b = randrange(100)
        if msg.content in RATE:
            possive = ["a"]
            negative = ["gay", "ばか", "白痴", "on9", "6uo"]
            if msg.content in negative:
                passid = [626419302232227841]
                if msg.author.id not in passid:
                    if a >= b:
                        if a >= 50:
                            await msg.channel.send("YES," + str(a) + "%")
                        elif a < 50:
                            await msg.channel.send("NO," + str(a) + "%")
                    if b > a:
                        if b >= 50:
                            await msg.channel.send("YES," + str(b) + "%")
                        elif b < 50:
                            await msg.channel.send("NO," + str(b) + "%")
                elif msg.author.id in passid:
                    if a <= b:
                        if a >= 50:
                            await msg.channel.send("YES," + str(a) + "%")
                        elif a < 50:
                            await msg.channel.send("NO," + str(a) + "%")
                    if b < a:
                        if b >= 50:
                            await msg.channel.send("YES," + str(b) + "%")
                        elif b < 50:
                            await msg.channel.send("NO," + str(b) + "%")
            else:
                if b >= 50:
                    await msg.channel.send("YES," + str(b) + "%")
                elif b < 50:
                    await msg.channel.send("NO," + str(b) + "%")
def setup(bot):
    bot.add_cog(rate(bot))