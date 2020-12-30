import discord
from discord.ext import commands
from useful import defcl, prefix
class Avatar(commands.Cog):
    """Show user avatar"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases = ['Avatarka', 'avatarka', 'Ava', 'ava', 'Avatar', 'avatar', 'Аватарка', 'аватарка', 'Ава', 'ава', 'Аватар', 'аватар'])
    async def __avatar(self, ctx, member: discord.Member = None):
        user = ctx.message.author if (member == None) else member
        emb = discord.Embed(title = f'Аватар пользователя {user}', color = defcl['avatar'])
        emb.set_image(url = user.avatar_url)
        await ctx.send(embed = emb)
        print(f'[Logs:utils] Аватар пользователя {user} был выведен | {prefix}avatar')
def setup(bot):
    bot.add_cog(Avatar(bot))