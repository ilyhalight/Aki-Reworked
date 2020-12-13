import discord
import config
from discord.ext import commands
from config import cogs_color
from useful import prefix, translit_abc, copyright_ru
class Translit(commands.Cog):
    """Translates translit into Russian text"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases = ['Translit', 'translit', 'Транслит', 'транслит'])
    async def __translit(self, ctx, *, message = None):
        if message == None:
            emb = discord.Embed(description = f'Пример: `{prefix}транслит privet` - Будет выведено сообщение привет.', color = cogs_color['TRANSLIT COLOR EXAMPLE'])
            emb.set_footer(text = copyright_ru, icon_url = self.bot.user.avatar_url)
            await ctx.send(embed = emb)
            print(f'[Logs:error] Один из аргументов не был введен корректно | {prefix}транслит [RU]')
        else:
            itog = ""
            errors = ""
            for i in message:
                if i.lower() in translit_abc:
                    itog += translit_abc[i.lower()]
                else:
                    errors += f"`{i}` "
            if len(errors) <= 0:
                 errors_itog = ""
            else:
                errors_itog = f"\nНепереведенные символы: {errors}"
                print(f"[Logs:utils] [Warning] Перевод содержит непереведенные символы | {prefix}транслит [RU]")

            if len(itog) <= 0:
                emb = discord.Embed(description = 'Не удалось перевести сообщение! :pencil:\nВозможно, вы пытаетесь перевести русское слово в транслит', color = cogs_color['TRANSLIT COLOR ERROR'])
                emb.set_footer(text = copyright_ru, icon_url = self.bot.user.avatar_url)
                await ctx.send(embed = emb)
                print(f"[Logs:utils] [Error] Не удалось перевести сообщение | {prefix}транслит [RU]")
            else:
                itog_new = f"Перевод: {itog}"
                emb = discord.Embed(description = f'{itog_new}{errors_itog}', color = cogs_color['LAYOUT COLOR EXAMPLE'])
                emb.set_footer(text = copyright_ru, icon_url = self.bot.user.avatar_url)
                await ctx.send(embed = emb)
                print(f"[Logs:utils] Текст был успешно переведен на русскую раскладку | {prefix}транслит [RU]")
def setup(bot):
    bot.add_cog(Translit(bot))