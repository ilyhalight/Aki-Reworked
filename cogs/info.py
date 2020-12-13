import discord
import config
from discord.ext import commands
from config import cogs_color, settings, other_settings
from useful import prefix, copyright_ru
class Info(commands.Cog):
    """Show bot info"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases = ['Info', 'info', 'Bot', 'bot', 'Bot_info', 'bot_info', 'Botinfo', 'botinfo', 'Инфо', 'инфо', 'Бот', 'бот', 'Бот_инфо', 'бот_инфо', 'Ботинфо', 'ботинфо'])
    async def __botinfo (self, ctx):
        emb = discord.Embed(title = ctx.guild.name, description = f'Информация о боте **{self.bot.user.name}**.\nПодробнее о командах - `{prefix}хелп`', color = cogs_color['BOT INFO COLOR'])
        emb.add_field(name = f'Меня создал:', value = settings['OWNER'], inline = True)
        emb.add_field(name = f'Отдельное спасибо:', value = settings['SPECIAL THANKS'], inline = True)
        emb.add_field(name = f'Лицензия:', value = 'CC CM-KD-QV', inline = True)
        emb.add_field(name = f'Версия:', value = other_settings['CURRENT VERSION'], inline = True)
        emb.add_field(name = f'Патч:', value = other_settings['CURRENT PATCH'], inline = True)
        emb.set_thumbnail(url = self.bot.user.avatar_url)
        emb.set_footer(text = copyright_ru, icon_url = self.bot.user.avatar_url)
        await ctx.send(embed = emb)
        print(f"[Logs:info] Информация о боте была успешно выведена | {prefix}инфо")
def setup(bot):
    bot.add_cog(Info(bot))