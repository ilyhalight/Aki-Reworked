import discord
import config
from discord.ext import commands
from config import cogs_color
from useful import prefix, copyright_en
class Reverse_Text(commands.Cog):
    """does reverse text"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases = ['Reverse', 'reverse', 'Реверс', 'реверс', 'Обратный', 'обратный'])
    async def __reverse(self, ctx, *, text: str):
        t_rev = text[::-1].replace("@", "@\u200B").replace("&", "&\u200B")
        emb = discord.Embed(title = 'Reverse text:', description = t_rev, color = cogs_color["REVERSE COLOR"])
        emb.set_footer(text = copyright_en, icon_url = self.bot.user.avatar_url)
        await ctx.send(embed = emb)
        print(f"[Logs:utils] Команда была успешно использована | {prefix}reverse [EU]"
def setup(bot):
    bot.add_cog(Reverse_Text(bot))