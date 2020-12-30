import discord
from discord.ext import commands
from useful import exacl, prefix, copyright_ru
class Del_emoji(commands.Cog):
    """Remove emoji from message"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases = ['Del_emoji', 'del_emoji', 'Del_reaction', 'del_reaction', 'Delete_emoji', 'delete_emoji', 'Delete_reaction', 'delete_reaction', 'Remove_emoji', 'remove_emoji', 'Remove_reaction', 'remove_reaction',  'Дел_эмодзи', 'дел_эмодзи', 'Дел_эмоджи', 'дел_эмоджи', 'Дел_реакцию', 'дел_реакцию', 'Удалить_эмоджи', 'удалить_эмоджи', 'Удалить_реакцию', 'удалить_реакцию'])
    @commands.has_permissions(administrator = True)
    async def __delemoji(self, ctx, id: int = None, reaction: str = None, member: discord.Member = None):
        if id != None and reaction != None:
            user = ctx.message.author if (member == None) else member # Если member не указан, то им будет автор сообщения
            await ctx.message.delete()
            message = await ctx.message.channel.fetch_message(id)
            await message.remove_reaction(reaction, user) # Удалить конкретную реакцию, конкретного пользователя в кокретном сообщение
            print(f"[Logs:owner] Отправленное пользователем {user} эмоджи было удалено для сообщения - [{id}] | {prefix}delete_emoji")
        else:
            emb = discord.Embed(description = f'Пример: `{prefix}удалить_эмодзи <id сообщения> <эмоджи> [@Пользователь]` - Удалить конкретные эмоджи пользователя в сообщение.', color = exacl['delete emoji'])
            emb.set_footer(text = copyright_ru, icon_url = self.bot.user.avatar_url)
            await ctx.send(embed = emb)
            print(f'[Logs:error] Один из аргументов не был введен корректно | {prefix}delete_emoji')

def setup(bot):
    bot.add_cog(Del_emoji(bot))