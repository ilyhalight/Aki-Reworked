import discord
import useful, config
from discord.ext import commands
from random import choice as randchoice
from useful import fucku_ru, prefix
from config import cogs_color
class Fuck(commands.Cog):
    """Display fuck you statements"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases = ['Fuckyou', 'fuckyou', 'Fucku', 'fucku', 'Послать', 'послать', 'Факю', 'факю'])
    async def __fuckyou(self, ctx, user: discord.Member = None):
        auth = ctx.message.author
        if not user:
            emb = discord.Embed(color = cogs_color['FUCK U NOT USER'])
            emb.add_field(name = "Ошибка:warning:", value = "Вы должны упомянуть пользователя, {}".format(auth.mention))
            await ctx.send(embed = emb)
        else:
            fuck = randchoice(useful.fucku_ru).format(user.mention, auth.mention)
            emb = discord.Embed(color = cogs_color['FUCK U'])
            emb.add_field(name = "Послать!:middle_finger:", value = "{}".format(fuck))
            await ctx.send(embed = emb)
def setup(bot):
    bot.add_cog(Fuck(bot))