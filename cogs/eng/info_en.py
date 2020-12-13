import discord
import config
from discord.ext import commands
from config import cogs_color, settings, quick_messages, other_settings
from useful import prefix, copyright_en
class Info(commands.Cog):
    """Show bot info"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases = ['Info', 'info', 'Bot', 'bot', 'Bot_info', 'bot_info', 'Botinfo', 'botinfo', 'Инфо', 'инфо', 'Бот', 'бот', 'Бот_инфо', 'бот_инфо', 'Ботинфо', 'ботинфо'])
    async def __botinfo (self, ctx):
        emb = discord.Embed(title = ctx.guild.name, description = f'Bot information about the **{self.bot.user.name}**.\nMore about commands - `{prefix}help`', color = cogs_color['BOT INFO COLOR'])
        emb.add_field(name = f'Created me:', value = settings['OWNER'], inline = True)
        emb.add_field(name = f'Special thanks to:', value = settings['SPECIAL THANKS'], inline = True)
        emb.add_field(name = f'License:', value = 'CC CM-KD-QV', inline = True)
        emb.add_field(name = f'Version:', value = other_settings['CURRENT VERSION'], inline = True)
        emb.add_field(name = f'Patch:', value = other_settings['CURRENT PATCH'], inline = True)
        emb.set_thumbnail(url = self.bot.user.avatar_url)
        emb.set_footer(text = copyright_en, icon_url = self.bot.user.avatar_url)
        await ctx.send(embed = emb)
        print(f"[Logs:info] Информация о боте была успешно выведена | {prefix}info")
def setup(bot):
    bot.add_cog(Info(bot))