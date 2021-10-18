import discord
from discord.ext import commands
from core.classes import Cog_Extension

class Main(Cog_Extension):

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'{round(self.bot.latency*1000)} ms')

    @commands.command()
    async def gary(self, ctx):
        await ctx.send("1600(Mon,Tue,Wed,Fri);1600-1700&2000(Thu);1900(Sat);1500(Sun)")
        print("sameone asked gary")

    @commands.command()
    async def garypc(self, ctx):
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
        print("sameone asked gary's PC")


def setup(bot):
    bot.add_cog(Main(bot))