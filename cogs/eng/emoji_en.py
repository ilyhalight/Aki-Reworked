import discord
import config
from discord.ext import commands
from config import cogs_color
from useful import prefix, copyright_en
class Emoji(commands.Cog):
    """Add emoji to message"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases = ['Emoji', 'emoji', 'Reaction', 'reaction', 'Эмодзи', 'эмодзи', 'Эмоджи', 'эмоджи', 'Реакция', 'реакция'])
    @commands.has_permissions(administrator = True)
    async def __emoji(self, ctx, id: int = None, reaction: str = None):
        if id != None and reaction != None:
            await ctx.message.delete()
            message = await ctx.message.channel.fetch_message(id)
            await message.add_reaction(reaction) # Добавить реакцию к сообщению
            print(f'[Logs:owner] К сообщению [{id}] была добавлена эмоджи | {prefix}emoji')
        else:
            emb = discord.Embed(description = f'Example: `{prefix}emoji <message id> <emoji>` - Add emoji to message.', color = cogs_color['ADD EMOJI COLOR EXAMPLE'])
            emb.set_footer(text = copyright_en, icon_url = self.bot.user.avatar_url)
            await ctx.send(embed = emb)
            print(f'[Logs:error] Один из аргументов не был введен корректно | {prefix}emoji')
def setup(bot):
    bot.add_cog(Emoji(bot))