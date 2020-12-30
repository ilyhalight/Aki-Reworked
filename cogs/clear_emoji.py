import discord
from discord.ext import commands
from useful import exacl, prefix, copyright_ru
class Clear_emoji(commands.Cog):
    """Remove specific emoji from message"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases = ['Clear_emoji', 'clear_emoji', 'Clear_reaction', 'clear_reaction', 'Стереть_эмодзи', 'стереть_эмодзи', 'Стереть_эмоджи', 'стереть_эмоджи', 'Стереть_реакцию', 'стереть_реакцию'])
    @commands.has_permissions(administrator = True)
    async def __clearemoji(self, ctx, id: int = None, reaction: str = None):
        if id != None and reaction != None:
            await ctx.message.delete()
            message = await ctx.message.channel.fetch_message(id)
            await message.clear_reaction(reaction) # Удалить определенные реакции к сообщению
            print(f"[Logs:owner] В сообщение [{id}] были очищенны определенные эмоджи | {prefix}clear_emoji")
        else:
            emb = discord.Embed(description = f'Пример: `{prefix}Стереть_эмодзи <id сообщения> <эмоджи>` - Стереть конкретные эмоджи в сообщение.', color = exacl['clear emoji'])
            emb.set_footer(text = copyright_ru, icon_url = self.bot.user.avatar_url)
            await ctx.send(embed = emb)
            print(f'[Logs:error] Один из аргументов не был введен корректно | {prefix}clear_emoji')
def setup(bot):
    bot.add_cog(Clear_emoji(bot))