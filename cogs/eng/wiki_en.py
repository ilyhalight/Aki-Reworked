import discord
import wikipedia, config
from discord.ext import commands
from config import cogs_color, quick_messages, fast_link
from useful import prefix, copyright_en
unknown_log = quick_messages['UNKNOWN ERROR LOG']
unknown_en = quick_messages['UNKNOWN ERROR EN']
class Wikipedia(commands.Cog):
    """Find out information about anything using Wikipedia"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases = ['Wiki', 'wiki', 'Wikipedia', 'wikipedia', 'Вики', 'вики', 'Википедия', 'википедия'])
    async def __wiki(self, ctx, *, text = None):
        if text == None:
            emb = discord.Embed(description = f'Example: `{prefix}wiki discord` - Find information about discord on wikipedia.')
            emb.set_footer(text = copyright_en, icon_url = self.bot.user.avatar_url)
            await ctx.send(embed = emb)
            print(f'[Logs:error] Искомая информация не была введена | {prefix}wiki')
        else:
            try:
                wikipedia.set_lang('eu')
                new_page = wikipedia.page(text)
                summ = wikipedia.summary(text)
                emb = discord.Embed(title = new_page.title, description = summ, color = cogs_color['WIKIPEDIA COLOR'])
                emb.set_author(name = 'More information here! Click!', url = new_page.url, icon_url = fast_link['WIKIPEDIA IMG'])
                emb.set_footer(icon_url = self.bot.user.avatar_url, text = copyright_en)
                await ctx.send(embed = emb)
                print(f'[Logs:utils] Информация о "{text}" была выведена | {prefix}wiki')
            except:
                emb = discord.Embed(description = unknown_en, color = cogs_color['WIKIPEDIA COLOR ERROR'])
                emb.set_footer(text = copyright_en, icon_url = self.bot.user.avatar_url)
                await ctx.send(embed = emb)
                print(f'{unknown_log} {prefix}wiki')
def setup(bot):
    bot.add_cog(Wikipedia(bot))