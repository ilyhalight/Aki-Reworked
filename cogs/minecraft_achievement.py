import discord
import random
from discord.ext import commands
from useful import errcl, links, defcl, prefix, copyright_ru
class Minecraft_achievement(commands.Cog):
    """Shows minecraft achievement with your text"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases = ['Achievement', 'achievement', 'Mine_achievement', 'mine_achievement', 'Mcach' ,'mcach', 'Ачивка', 'ачивка', 'Достижение', 'достижение', 'Майн_ачивка', 'майн_ачивка'])
    async def __minecraft_achievement(self, ctx, *, name:str = None):
        auth = ctx.message.author
        if name != None:
            a = random.randint(1, 40)
            name2 = name.replace(' ', '+')
            url = f'{links["mcach"]}{a}/Achievement+Get%21/{name2}'
            emb = discord.Embed(description = f'[Достижение!]({url})', color = defcl["mcach"])
            emb.set_footer(text = copyright_ru, icon_url = self.bot.user.avatar_url)
            emb.set_image(url = url)
            await ctx.send(embed = emb)
            print(f'[Logs:utils] Майнкрафт достижение было успешно создано | {prefix}achievement')
        else:
            emb = discord.Embed(color = errcl['mcach'])
            emb.add_field(name = "Ошибка:warning:", value = "Вы должны написать какой-нибудь текст, {}".format(auth.mention))
            await ctx.send(embed = emb)
def setup(bot):
    bot.add_cog(Minecraft_achievement(bot))