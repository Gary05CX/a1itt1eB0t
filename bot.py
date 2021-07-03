import discord
from discord.ext import commands

intents = discord.Intents.all()

bot = commands.Bot(command_prefix='?',intents=intents)

@bot.event
async def on_ready():
    print(">> a1itt1ebot is online!!! <<")
    channel = bot.get_channel(860843545387859979)
    await channel.send("a1itt1eB1t is online")

@bot.event
async def on_member_join(member):
    print(f"{member} join!")
    channel = bot.get_channel(860843545387859979)
    await channel.send(f"{member} join!")

@bot.event
async def on_member_remove(member):
    print(f"{member} leave!")
    channel = bot.get_channel(860843545387859979)
    await channel.send(f"{member} leave!")

bot.run('ODYwNTU0NTY0NTA3OTI2NTg4.YN875A.6ibKkKNESjNNl9cy-EA3nUo1t6A')