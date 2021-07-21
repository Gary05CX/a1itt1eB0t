import discord
from discord.ext import commands
from core.classes import Cog_Extension

class react(Cog_Extension):

    @commands.Cog.listener()
    async def on_message(self, msg):
        wife = ["老婆", "my wife"]
        id = [626419302232227841, 723473163341791314]
        if msg.content in wife:
            if msg.author.id not in id:
                await msg.add_reaction("<:wake_up:831196189407576134>")

def setup(bot):
    bot.add_cog(react(bot))