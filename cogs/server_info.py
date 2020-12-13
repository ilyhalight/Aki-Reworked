import discord
import config
from discord.ext import commands
from config import cogs_color
from useful import prefix, copyright_ru
class Server_info(commands.Cog):
    """Shows information about the server"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases = ['Server', 'server', 'Server_info', 'server_info', 'Serverinfo', 'serverinfo', 'Сервер', 'сервер', 'Сервер_инфо', 'сервер_инфо', 'Серверинфо', 'серверинфо']) # Thanks Fsoky community
    async def __serverinfo(self, ctx):
        allchannels = len(ctx.guild.channels)
        allvoice = len(ctx.guild.voice_channels)
        alltext = len(ctx.guild.text_channels)
        allroles = len(ctx.guild.roles)
        emb = discord.Embed(title = ctx.guild.name, color = cogs_color['SERVER INFO COLOR'], timestamp = ctx.message.created_at)
        emb.description=(
            f":timer: Сервер создали: **{ctx.guild.created_at.strftime('%A, %b %#d %Y')}**\n\n"
            f":flag_white: Регион: **{ctx.guild.region}\n\n"
            f":crown: Глава сервера **{ctx.guild.owner}**\n\n"
            f":shield: Уровень верификации: **{ctx.guild.verification_level}**\n\n"
            f":musical_keyboard: Всего каналов: **{allchannels}**\n\n"
            f":loud_sound: Голосовых каналов: **{allvoice}**\n\n"
            f":keyboard: Текстовых каналов: **{alltext}**\n\n"
            f":briefcase: Всего ролей: **{allroles}**\n\n"
            f":slight_smile: Людей на сервере: **{ctx.guild.member_count}\n\n"
        )
        emb.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
        emb.set_thumbnail(url = self.bot.user.avatar_url)
        emb.set_footer(text = copyright_ru, icon_url = self.bot.user.avatar_url)
        await ctx.send(embed = emb)
        print(f"[Logs:info] Информация о сервере была успешно выведена | {prefix}сервер_инфо ")
def setup(bot):
    bot.add_cog(Server_info(bot))