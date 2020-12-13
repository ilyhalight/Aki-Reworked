import discord
import config
from discord.ext import commands
from config import cogs_color
from useful import prefix, copyright_en
class Ahelp(commands.Cog):
    """Show admin commands"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases = ['Ahelp', 'ahelp', 'Admin_help', 'admin_help', 'Adminhelp', 'adminhelp', 'Ахелп', 'ахелп', 'Админ_хелп', 'админ_хелп', 'Админхелп', 'админхелп'])
    @commands.is_owner()
    async def __ahelp(self, ctx):
            emb = discord.Embed(title = f'Available commands:', description = f'**Prefix: `{prefix}`**', color = cogs_color['AHELP COLOR'])
            emb.add_field(name = f'{prefix}emoji', value = f'Add emoji to message', inline = False)
            emb.add_field(name = f'{prefix}del_emoji', value = f'Remove specific user emoji from a message', inline = False)
            emb.add_field(name = f'{prefix}clear_emoji', value = f'Remove all specific emojis from a message', inline = False)
            emb.add_field(name = f'{prefix}clear_all_emoji', value = f'Will remove absolutely all emoji from the message', inline = False)
            emb.add_field(name = f'{prefix}bot_status', value = f'Set temporary status for the bot', inline = False)
            emb.set_thumbnail(url = self.bot.user.avatar_url)
            emb.set_footer(text = copyright_en, icon_url = self.bot.user.avatar_url)
            await ctx.send(embed = emb)
            print(f'[Logs:info] Админская сводка команд была выведена | {prefix}ahelp')
def setup(bot):
    bot.add_cog(Ahelp(bot))