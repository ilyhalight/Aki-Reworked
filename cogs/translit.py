import discord
from discord.ext import commands
from useful import exacl, errcl, prefix, translit_abc, copyright_ru
class Translit(commands.Cog):
    """Translates translit into Russian text"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases = ['Translit', 'translit', 'Транслит', 'транслит'])
    async def __translit(self, ctx, *, message = None):
        if message == None:
            emb = discord.Embed(description = f'Пример: `{prefix}транслит privet` - Будет выведено сообщение привет.', color = exacl['translit'])
            emb.set_footer(text = copyright_ru, icon_url = self.bot.user.avatar_url)
            await ctx.send(embed = emb)
            print(f'[Logs:error] Один из аргументов не был введен корректно | {prefix}транслит')
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
                print(f"[Logs:utils] [Warning] Перевод содержит непереведенные символы | {prefix}транслит")

            if len(itog) <= 0:
                emb = discord.Embed(description = 'Не удалось перевести сообщение! :pencil:\nВозможно, вы пытаетесь перевести русское слово в транслит', color = errcl['translit'])
                emb.set_footer(text = copyright_ru, icon_url = self.bot.user.avatar_url)
                await ctx.send(embed = emb)
                print(f"[Logs:utils] [Error] Не удалось перевести сообщение | {prefix}транслит")
            else:
                itog_new = f"Перевод: {itog}"
                emb = discord.Embed(description = f'{itog_new}{errors_itog}', color = exacl['translit'])
                emb.set_footer(text = copyright_ru, icon_url = self.bot.user.avatar_url)
                await ctx.send(embed = emb)
                print(f"[Logs:utils] Текст был успешно переведен на русскую раскладку | {prefix}транслит")
def setup(bot):
    bot.add_cog(Translit(bot))