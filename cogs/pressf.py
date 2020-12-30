import discord
import asyncio
from discord.ext import commands
from useful import exacl
class PressF(commands.Cog):
    """You can now pay repect to a person"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases = ['PressF', 'pressF', 'Pressf', 'pressf', 'F', 'f', 'ПрессФ', 'прессФ', 'Прессф', 'прессф', 'Ф', 'ф', 'Прессf', 'прессf', 'ПрессF', 'прессF'])
    async def __pressf(self, ctx, user: discord.User = None):
        author = ctx.message.author
        channel = ctx.message.channel
        if not user:
            emb = discord.Embed(color = exacl['press f'])
            emb.add_field(name = "Ошибка:warning:", value = "Вы должны упомянуть пользователя, {}".format(author.mention))
            await ctx.send(embed = emb)
        else:
            answer = user.display_name
            msg = "Все, давайте отдадим дань уважения ** {} **! Нажмите f реакцию под этим сообщением, чтобы отдать дань уважения.".format(answer)
            message = await ctx.send(msg)

            try:
                await ctx.message.add_reaction("🇫")
                react = True
            except:
                react = False
                await message.edit(content = "Все, давайте отдадим дань уважения ** {} **! Поставьте `f` в ответ на это сообщение, чтобы отдать дань уважения.".format(answer))

            await asyncio.sleep(120)
            await message.edit(content = "Спасибо всем, кто отдал респект ** {} **".format(answer))
def setup(bot):
    bot.add_cog(PressF(bot))