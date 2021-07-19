from discord.ext import commands
from core.classes import Cog_Extension 

class yag(Cog_Extension):

    @commands.Cog.listener()
    async def on_message(self, msg):
        keyword = ["男上加男","強人所男","勉為騎男","知男而上","左右為男","男男自語","千載男逢","男分男捨","面有男色","知易行男","自身男保","寸步男行","大男不死","大男臨頭","插翅男逃","暗箭男防","百年男遇","百般叼男","覆水男收","本性男移","在劫男逃","進退兩男","男能可貴","騎虎男下","排除萬男","知男而退","天理男容","肆碼男追","盛情男怯","男已理解","一言男進","男如登天","男以自拔"]
        if msg.content in keyword and msg.author != self.bot.user:
            await msg.channel.send("""你可能感興趣的關鍵字：
男上加男
強人所男
勉為騎男
知男而上
左右為男
男男自語
千載男逢
男分男捨
面有男色
知易行男
自身男保
寸步男行
大男不死
大男臨頭
插翅男逃
暗箭男防
百年男遇
百般叼男
覆水男收
本性男移
在劫男逃
進退兩男
男能可貴
騎虎男下
排除萬男
知男而退
天理男容
肆碼男追
盛情男怯
男已理解
一言男進
男如登天
男以自拔""")

def setup(bot):
    bot.add_cog(yag(bot))