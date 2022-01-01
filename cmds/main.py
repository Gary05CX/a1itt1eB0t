import discord
from discord.ext import commands
from discord.ext.commands.core import command
from core.classes import Cog_Extension
import time as t

class Main(Cog_Extension):

    @commands.command()
    async def ping(self, ctx):
        id = str(ctx.author.id)
        local = t.localtime()
        time = t.strftime("%Y %m %d %H:%M:%S", local)
        cmd = str("ping")
        await ctx.send(f'{round(self.bot.latency*1000)} ms')
        with open("C:\Discord Bot\Project_1\\a1itt1eB0t\\note.txt", mode="a", encoding="utf-8") as file:
            file.write("\n")
            file.write("\n")
            file.write(time)
            file.write("\n")
            file.write(id)
            file.write("\n")
            file.write(cmd)

    @commands.command()
    async def gary(self, ctx):
        id = str(ctx.author.id)
        local = t.localtime()
        time = t.strftime("%Y %m %d %H:%M:%S", local)
        cmd = str("gary")
        await ctx.send("....")
        with open("C:\Discord Bot\Project_1\\a1itt1eB0t\\note.txt", mode="a", encoding="utf-8") as file:
            file.write("\n")
            file.write("\n")
            file.write(time)
            file.write("\n")
            file.write(id)
            file.write("\n")
            file.write(cmd)

    @commands.command()
    async def garypc(self, ctx):
        id = str(ctx.author.id)
        local = t.localtime()
        time = t.strftime("%Y %m %d %H:%M:%S", local)
        cmd = str("garypc")
        await ctx.send("""Motherboard: ASRock B550 Steel Legend ATX
CPU: AMD Ryzen 7 3700X 
GPU: GEFORCE GTX 1660 SUPER VENTUS XS OC
RAM: ADATA XPG GAMMIX D10 DDR 3200 MHz 16GB x 2
SSD: ADATA XPG SX8200 PRO 1TB 3D TLC M.2 NVMe PCIe 3.0 x4 SSD
PSU: Antec Neo Eco Gold 750W 80Plus Gold X (7) x 1
Case: Cooler Master NR600 ATX Case 
Mouse: Logitech G pro superlight / G502 Lightspeed
Keyboard: Logitech G512
Mic: HyperX QuadCast S
Headphone: Razer Kraken + Razer USB Audio Controller
Monitor: ZOWIE XL2411P 144Hz""")
        with open("C:\Discord Bot\Project_1\\a1itt1eB0t\\note.txt", mode="a", encoding="utf-8") as file:
            file.write("\n")
            file.write("\n")
            file.write(time)
            file.write("\n")
            file.write(id)
            file.write("\n")
            file.write(cmd)

    @commands.command()
    async def say(self, ctx, *, msg):
        id = str(ctx.author.id)
        local = t.localtime()
        time = t.strftime("%Y %m %d %H:%M:%S", local)
        cmd = str("say")
        await ctx.message.delete()
        await ctx.send(msg)
        with open("C:\Discord Bot\Project_1\\a1itt1eB0t\\note.txt", mode="a", encoding="utf-8") as file:
            file.write("\n")
            file.write("\n")
            file.write(time)
            file.write("\n")
            file.write(id)
            file.write("\n")
            file.write(cmd)

    @commands.command()
    async def time(self, ctx):
        id = str(ctx.author.id)
        cmd = str("time")
        local = t.localtime()
        time = t.strftime("%Y %m %d %H:%M:%S", local)
        await ctx.send(time)
        with open("C:\Discord Bot\Project_1\\a1itt1eB0t\\note.txt", mode="a", encoding="utf-8") as file:
            file.write("\n")
            file.write("\n")
            file.write(time)
            file.write("\n")
            file.write(id)
            file.write("\n")
            file.write(cmd)

def setup(bot):
    bot.add_cog(Main(bot))