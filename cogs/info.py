import discord
from discord.ext import commands
from useful import other, defcl, prefix, copyright_ru
class Info(commands.Cog):
    """Show bot info"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases = ['Info', 'info', 'Bot', 'bot', 'Bot_info', 'bot_info', 'Botinfo', 'botinfo', 'Инфо', 'инфо', 'Бот', 'бот', 'Бот_инфо', 'бот_инфо', 'Ботинфо', 'ботинфо'])
    async def __botinfo (self, ctx):
        emb = discord.Embed(title = ctx.guild.name, description = f'Информация о боте **{self.bot.user.name}**.\nПодробнее о командах - `{prefix}хелп`', color = defcl['bot info'])
        emb.add_field(name = f'Меня создал:', value = other['owner'], inline = True)
        emb.add_field(name = f'Отдельное спасибо:', value = other['special thanks'], inline = True)
        emb.add_field(name = f'Лицензия:', value = other['license'], inline = True)
        emb.add_field(name = f'Версия:', value = other['version'], inline = True)
        emb.add_field(name = f'Патч:', value = other['patch'], inline = True)
        emb.set_thumbnail(url = self.bot.user.avatar_url)
        emb.set_footer(text = copyright_ru, icon_url = self.bot.user.avatar_url)
        await ctx.send(embed = emb)
        print(f"[Logs:info] Информация о боте была успешно выведена | {prefix}инфо")
def setup(bot):
    bot.add_cog(Info(bot))