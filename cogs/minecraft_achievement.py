import discord
import random, config
from discord.ext import commands
from config import cogs_color, fast_link
from useful import prefix, copyright_ru
class Minecraft_achievement(commands.Cog):
    """Shows minecraft achievement with your text"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases = ['Achievement', 'achievement', 'Mine_achievement', 'mine_achievement', 'Ачивка', 'ачивка', 'Достижение', 'достижение', 'Майн_ачивка', 'майн_ачивка'])
    async def __minecraft_achievement(self, ctx, *, name:str = None):
        a = random.randint(1, 40)
        name2 = name.replace(' ', '+')
        url = f'{fast_link["MCACH"]}{a}/Achievement+Get%21/{name2}'
        emb = discord.Embed(description = f'[Достижение!]({url})', color = cogs_color["MCACH COLOR"])
        emb.set_footer(text = copyright_ru, icon_url = self.bot.user.avatar_url)
        emb.set_image(url = url)
        await ctx.send(embed = emb)
        print(f'[Logs:utils] Майнкрафт достижение было успешно создано | {prefix}achievement')
def setup(bot):
    bot.add_cog(Minecraft_achievement(bot))