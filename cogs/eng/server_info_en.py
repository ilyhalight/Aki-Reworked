import discord
import config
from discord.ext import commands
from config import cogs_color
from useful import prefix, copyright_en
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
            f":timer: Server created: **{ctx.guild.created_at.strftime('%A, %b %#d %Y')}**\n\n"
            f":flag_white: Region: **{ctx.guild.region}\n\n"
            f":crown: Server creator **{ctx.guild.owner}**\n\n"
            f":shield:  Verification level: **{ctx.guild.verification_level}**\n\n"
            f":musical_keyboard: Total channels: **{allchannels}**\n\n"
            f":loud_sound: Voice channels: **{allvoice}**\n\n"
            f":keyboard: Text channels: **{alltext}**\n\n"
            f":briefcase: Total roles: **{allroles}**\n\n"
            f":slight_smile: Members: **{ctx.guild.member_count}\n\n"
        )
        emb.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
        emb.set_thumbnail(url = self.bot.user.avatar_url)
        emb.set_footer(text = copyright_en, icon_url = self.bot.user.avatar_url)
        await ctx.send(embed = emb)
        print(f"[Logs:info] Информация о сервере была успешно выведена | {prefix}server ")
def setup(bot):
    bot.add_cog(Server_info(bot))