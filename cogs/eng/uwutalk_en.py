import discord
import useful
from discord.ext import commands
from random import choice as randchoice
from useful import uwutalk_en, prefix
class Uwutalk(commands.Cog):
    """Get uwu you statements"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases = ['Uwutalk', 'uwutalk', 'Увутолк', 'увутолк'])
    async def __uwutalk(self, ctx, user: discord.Member = None):
        auth = ctx.message.author
        if not user:
            emb = discord.Embed(colour = auth.colour)
            emb.add_field(name = "Error:warning:", value = "You have to mention a user, {}".format(auth.mention))
            await ctx.send(embed = emb)
        else:
            uwu = randchoice(useful.uwutalk_en).format(user.mention, auth.mention)
            emb = discord.Embed(colour = 0xca3a3a)
            emb.add_field(name = "Uwutalk!:dizzy:", value="{}".format(uwu))
            await ctx.send(embed = emb)
def setup(bot):
    bot.add_cog(Uwutalk(bot))