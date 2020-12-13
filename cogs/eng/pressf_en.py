import discord
import asyncio, config
from discord.ext import commands
from config import cogs_color
from useful import prefix
class PressF(commands.Cog):
    """You can now pay repect to a person"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases = ['PressF', 'pressF', 'Pressf', 'pressf', 'F', 'f', 'ПрессФ', 'прессФ', 'Прессф', 'прессф', 'Ф', 'ф', 'Прессf', 'прессf', 'ПрессF', 'прессF'])
    async def __pressf(self, ctx, user: discord.User = None):
        author = ctx.message.author
        channel = ctx.message.channel
        if not user:
            emb = discord.Embed(color = cogs_color['FUCK U NOT USER'])
            emb.add_field(name = "Error:warning:", value = "You have to mention a user, {}".format(author.mention))
            await ctx.send(embed = emb)
        else:
            answer = user.display_name
            msg = "Everyone, let's pay respects to **{}**! Press f reaction on this message to pay respects.".format(answer)
            message = await ctx.send(msg)

            try:
                await ctx.message.add_reaction("🇫")
                react = True
            except:
                react = False
                await message.edit(content = "Everyone, let's pay respects to **{}**! Type `f` reaction on the this message to pay respects.".format(answer))

            await asyncio.sleep(120)
            await message.edit(content = "Thanks to everyone who gave respect to ** {} **".format(answer))
def setup(bot):
    bot.add_cog(PressF(bot))