import discord
import config
from discord.ext import commands
from config import cogs_color
from useful import prefix
class Avatar(commands.Cog):
    """Show user avatar"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases = ['Avatarka', 'avatarka', 'Ava', 'ava', 'Avatar', 'avatar', 'Аватарка', 'аватарка', 'Ава', 'ава', 'Аватар', 'аватар'])
    async def __avatar(self, ctx, member: discord.Member = None):
        user = ctx.message.author if (member == None) else member
        emb = discord.Embed(title = f'Аватар пользователя {user}', color = cogs_color['AVATAR COLOR'])
        emb.set_image(url = user.avatar_url)
        await ctx.send(embed = emb)
        print(f'[Logs:utils] Аватар пользователя {user} был выведен | {prefix}avatar')
def setup(bot):
    bot.add_cog(Avatar(bot))