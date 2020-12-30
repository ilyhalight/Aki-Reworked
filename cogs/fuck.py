import discord
from discord.ext import commands
from random import choice as randchoice
from useful import errcl, defcl, fucku_ru
class Fuck(commands.Cog):
    """Display fuck you statements"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases = ['Fuckyou', 'fuckyou', 'Fucku', 'fucku', 'Fuck', 'fuck', 'Послать', 'послать', 'Факю', 'факю'])
    async def __fuckyou(self, ctx, user: discord.Member = None):
        auth = ctx.message.author
        if not user:
            emb = discord.Embed(color = errcl['fuck you'])
            emb.add_field(name = "Ошибка:warning:", value = "Вы должны упомянуть пользователя, {}".format(auth.mention))
            await ctx.send(embed = emb)
        else:
            fuck = randchoice(fucku_ru).format(user.mention, auth.mention)
            emb = discord.Embed(color = defcl['fuck you'])
            emb.add_field(name = "Послать!:middle_finger:", value = "{}".format(fuck))
            await ctx.send(embed = emb)
def setup(bot):
    bot.add_cog(Fuck(bot))