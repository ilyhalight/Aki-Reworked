import discord
from discord.ext import commands
from useful import defcl, prefix, copyright_ru
class Ahelp(commands.Cog):
    """Show admin commands"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases = ['Ahelp', 'ahelp', 'Admin_help', 'admin_help', 'Adminhelp', 'adminhelp', 'Ахелп', 'ахелп', 'Админ_хелп', 'админ_хелп', 'Админхелп', 'админхелп'])
    @commands.is_owner()
    async def __ahelp(self, ctx):
            emb = discord.Embed(title = 'Доступные команды:', description = f'**Префикс: `{prefix}`**', color = defcl['ahelp'])
            emb.add_field(name = f'{prefix}эмоджи', value = 'Добавить эмоджи к сообщению', inline = False)
            emb.add_field(name = f'{prefix}удалить_эмоджи', value = 'Удалить конкретные эмоджи пользователя с сообщения', inline = False)
            emb.add_field(name = f'{prefix}стереть_эмодзи', value = 'Стереть конкретные эмоджи с сообщения', inline = False)
            emb.add_field(name = f'{prefix}стереть_все\се_эмодзи', value = 'Стереть абсолютно все эмоджи с сообщения', inline = False)
            emb.add_field(name = f'{prefix}бот_статус', value = 'Установить временный статус для бота', inline = False)
            emb.set_thumbnail(url = self.bot.user.avatar_url)
            emb.set_footer(text = copyright_ru, icon_url = self.bot.user.avatar_url)
            await ctx.send(embed = emb)
            print(f'[Logs:info] Админская сводка команд была выведена | {prefix}ахелп')
def setup(bot):
    bot.add_cog(Ahelp(bot))