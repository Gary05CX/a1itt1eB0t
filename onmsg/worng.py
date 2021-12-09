import discord
from discord.ext import commands
from core.classes import Cog_Extension
import time as t

class wrong(Cog_Extension):

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.errors.MissingRequiredArgument):
            id = str(ctx.author.id)
            local = t.localtime()
            time = t.strftime("%Y %m %d %H:%M:%S", local)
            cmd = str("Missing required argument")
            await ctx.send("Missing required argument 遺失參數!!")
            with open("C:\Discord Bot\Project_1\\a1itt1eB0t\\note.txt", mode="a", encoding="utf-8") as file:
                file.write("\n")
                file.write("\n")
                file.write(time)
                file.write("\n")
                file.write(id)
                file.write("\n")
                file.write(cmd)
        elif isinstance(error, commands.errors.CommandNotFound):
            id = str(ctx.author.id)
            local = t.localtime()
            time = t.strftime("%Y %m %d %H:%M:%S", local)
            cmd = str("Commands not found")
            await ctx.send("Commands not found  沒這指令!!")
            with open("C:\Discord Bot\Project_1\\a1itt1eB0t\\note.txt", mode="a", encoding="utf-8") as file:
                file.write("\n")
                file.write("\n")
                file.write(time)
                file.write("\n")
                file.write(id)
                file.write("\n")
                file.write(cmd)
        else:
            id = str(ctx.author.id)
            local = t.localtime()
            time = t.strftime("%Y %m %d %H:%M:%S", local)
            cmd = str("something goes wrong")
            await ctx.send("something goes wrong  發生錯誤!!!")
            with open("C:\Discord Bot\Project_1\\a1itt1eB0t\\note.txt", mode="a", encoding="utf-8") as file:
                file.write("\n")
                file.write("\n")
                file.write(time)
                file.write("\n")
                file.write(id)
                file.write("\n")
                file.write(cmd)

def setup(bot):
    bot.add_cog(wrong(bot))
