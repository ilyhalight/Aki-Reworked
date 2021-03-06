import discord
import random
from discord.ext import commands
from useful import quick_messages, errcl, defcl, prefix, copyright_ru
third_sym_log = quick_messages['THIRD PARTY SYM ERROR LOG']
class Random(commands.Cog):
    """Show random number"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases = ['Random', 'random', 'Rand', 'rand', 'Рандом', 'рандом', 'Ранд', 'ранд'])
    async def __random(self, ctx, count = None, count1 = None):
        if count == None and count1 == None:
            emb = discord.Embed(description = f'Пример: `{prefix}рандом 5` - Будет выведено число от 1 до 5.\n Пример 2: `{prefix}рандом 5 10` - Будет выведено число от 5 до 10.', color = defcl['random'])
            emb.set_footer(text = copyright_ru, icon_url = self.bot.user.avatar_url)
            await ctx.send(embed = emb)
            print(f'[Logs:utils] Максимальное число не было указано | {prefix}random')
        if count != None and count1 == None:
            try:
                await ctx.send(str(random.randint(int(1), int(count))))
                print(f'[Logs:utils] Рандомное число было успешно сгенерировано | {prefix}random')
            except ValueError:
                emb = discord.Embed(description = quick_messages['THIRD PARTY SYM ERROR'], color = errcl['random'])
                emb.set_footer(text = copyright_ru, icon_url = self.bot.user.avatar_url)
                await ctx.send(embed = emb)
                print(f'{third_sym_log} {prefix}random')
        if count != None and count1 != None:
            try:
                await ctx.send(str(random.randint(int(count), int(count1))))
                print(f'[Logs:utils] Рандомное число было успешно сгенерировано | {prefix}random')
            except ValueError:
                emb = discord.Embed(description = quick_messages['THIRD PARTY SYM ERROR'], color = errcl['random'])
                emb.set_footer(text = copyright_ru, icon_url = self.bot.user.avatar_url)
                await ctx.send(embed = emb)
                print(f'{third_sym_log} {prefix}random')
def setup(bot):
    bot.add_cog(Random(bot))