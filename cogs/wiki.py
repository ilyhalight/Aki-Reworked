import discord, wikipedia
from discord.ext import commands
from useful import errcl, defcl, links, quick_messages, prefix, copyright_ru
unknown_log = quick_messages['UNKNOWN ERROR LOG']
unknown = quick_messages['UNKNOWN ERROR']
class Wikipedia(commands.Cog):
    """Find out information about anything using Wikipedia"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases = ['Wiki', 'wiki', 'Wikipedia', 'wikipedia', 'Вики', 'вики', 'Википедия', 'википедия'])
    async def __wiki(self, ctx, *, text = None):
        if text == None:
            emb = discord.Embed(description = f'Пример: `{prefix}вики discord` - Будет выведена информация о дискорде.')
            emb.set_footer(text = copyright_ru, icon_url = self.bot.user.avatar_url)
            await ctx.send(embed = emb)
            print(f'[Logs:error] Искомая информация не была введена | {prefix}wiki')
        else:
            try:
                wikipedia.set_lang('ru')
                new_page = wikipedia.page(text)
                summ = wikipedia.summary(text)
                emb = discord.Embed(title = new_page.title, description = summ, color = defcl['wipipedia'])
                emb.set_author(name = 'Больше информации здесь! Кликай!', url = new_page.url, icon_url = links['wikipedia img'])
                emb.set_footer(icon_url = self.bot.user.avatar_url, text = copyright_ru)
                await ctx.send(embed = emb)
                print(f'[Logs:utils] Информация о "{text}" была выведена | {prefix}wiki')
            except:
                emb = discord.Embed(description = unknown, color = errcl['wikipedia'])
                emb.set_footer(text = copyright_ru, icon_url = self.bot.user.avatar_url)
                await ctx.send(embed = emb)
                print(f'{unknown_log} {prefix}wiki')
def setup(bot):
    bot.add_cog(Wikipedia(bot))