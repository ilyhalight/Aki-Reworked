import discord
import random, config
from discord.ext import commands
from config import cogs_color, quick_messages
from useful import prefix, copyright_en
third_sym_log = quick_messages['THIRD PARTY SYM ERROR LOG']
class Random(commands.Cog):
    """Show random number"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases = ['Random', 'random', 'Rand', 'rand', 'Рандом', 'рандом', 'Ранд', 'ранд'])
    async def __random(self, ctx, count = None, count1 = None):
        if count == None and count1 == None:
            emb = discord.Embed(description = f'Example: `{prefix}random 5` - Will print a number from 1 to 5.\n Example: `{prefix}random 5 10` - Will print a number from 5 to 10.', color = cogs_color['RANDOM COLOR'])
            emb.set_footer(text = copyright_en, icon_url = self.bot.user.avatar_url)
            await ctx.send(embed = emb)
            print(f'[Logs:utils] Максимальное число не было указано | {prefix}random')
        if count != None and count1 == None:
            try:
                await ctx.send(str(random.randint(int(1), int(count))))
                print(f'[Logs:utils] Рандомное число было успешно сгенерировано | {prefix}random')
            except ValueError:
                emb = discord.Embed(description = quick_messages['THIRD PARTY SYM ERROR EN'], color = cogs_color['RANDOM COLOR ERROR'])
                emb.set_footer(text = copyright_en, icon_url = self.bot.user.avatar_url)
                await ctx.send(embed = emb)
                print(f'{third_sym_log} {prefix}random')
        if count != None and count1 != None:
            try:
                await ctx.send(str(random.randint(int(count), int(count1))))
                print(f'[Logs:utils] Рандомное число было успешно сгенерировано | {prefix}random')
            except ValueError:
                emb = discord.Embed(description = quick_messages['THIRD PARTY SYM ERROR EN'], color = cogs_color['RANDOM COLOR ERROR'])
                emb.set_footer(text = copyright_en, icon_url = self.bot.user.avatar_url)
                await ctx.send(embed = emb)
                print(f'{third_sym_log} {prefix}random')
def setup(bot):
    bot.add_cog(Random(bot))