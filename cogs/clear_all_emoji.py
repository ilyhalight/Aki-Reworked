import discord
import config
from discord.ext import commands
from config import cogs_color
from useful import prefix, copyright_ru
class Clear_all_emoji(commands.Cog):
    """Erase all emojis in message"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases = ['Clear_all_emoji', 'clear_all_emoji', 'Clear_all_reactions', 'clear_all_reactions', 'Стереть_все_эмодзи', 'стереть_все_эмодзи', 'Стереть_все_эмоджи', 'стереть_все_эмоджи', 'Стереть_все_реакции', 'стереть_все_реакции'])
    @commands.is_owner()
    async def __clearallemoji(self, ctx, id: int = None):
        if id != None:
            await ctx.message.delete()
            message = await ctx.message.channel.fetch_message(id)
            await message.clear_reactions() # Очистить все реакции к сообщению
            print(f"[Logs:owner] В сообщение [{id}] были очищенны все эмоджи | {prefix}clear_all_emoji")
        else:
            emb = discord.Embed(description = f'Пример: `{prefix}Стереть_все_эмодзи <id сообщения>` - Стереть абсолютно все эмоджи в сообщение.', color = cogs_color['CLEAR ALL EMOJI COLOR EXAMPLE'])
            emb.set_footer(text = copyright_ru, icon_url = self.bot.user.avatar_url)
            await ctx.send(embed = emb)
            print(f'[Logs:error] Один из аргументов не был введен корректно | {prefix}clear_all_emoji')
def setup(bot):
    bot.add_cog(Clear_all_emoji(bot))