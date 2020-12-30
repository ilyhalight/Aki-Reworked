import discord
from discord.ext import commands
from useful import exacl, errcl, prefix, copyright_ru, ru_layout
class Forgot_layout(commands.Cog):
    """Forgot Layout"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases = ['Forgot_layout', 'forgot_layout', 'Forgotlayout', 'forgotlayout', 'Ru_layout', 'ru_layout', 'Rulayout', 'rulayout', 'Забыл_раскладку', 'забыл_раскладку', 'Забылраскладку', 'забылраскладку', 'Ру_раскладка', 'ру_раскладка', 'Рураскладка', 'рураскладка'])
    async def __Forgot_layout(self, ctx, *, message = None):
        if message == None:
            emb = discord.Embed(description = f'Пример: `{prefix}забыл_раскладку ghbdtn` - Появится сообщение "привет".', color = exacl['layout'])
            emb.set_footer(text = copyright_ru, icon_url = self.bot.user.avatar_url)
            await ctx.send(embed = emb)
            print(f'[Logs:error] Один из аргументов не был введен корректно | {prefix}ru_layout')
        else:
            itog = ""
            errors = ""
            for i in message:
                if i.lower() in ru_layout:
                    itog += ru_layout[i.lower()]
                else:
                    errors += f"`{i}` "
            if len(errors) <= 0:
                errors_itog = ""
            else:
                errors_itog = f"\nНепереведенные символы: {errors}"
                print(f"[Logs:utils] [Warning] Перевод содержит непереведенные символы | {prefix}ru_layout")

            if len(itog) <= 0:
                emb = discord.Embed(description = 'Не удалось перевести сообщение! :pencil:\nВозможно, вы пытаетесь перевести транслит в русское слово', color = errcl['layout'])
                emb.set_footer(text = copyright_ru, icon_url = self.bot.user.avatar_url)
                await ctx.send(embed = emb)
                print(f"[Logs:utils] [Error] Не удалось перевести сообщение | {prefix}ru_layout")
            else:
                itog_new = f"Перевод: {itog}"
                emb = discord.Embed(description = f'{itog_new}{errors_itog}', color = exacl['layout'])
                emb.set_footer(text = copyright_ru, icon_url = self.bot.user.avatar_url)
                await ctx.send(embed = emb)
                print(f"[Logs:utils] Текст был успешно переведен на русскую раскладку | {prefix}ru_layout")
def setup(bot):
    bot.add_cog(Forgot_layout(bot))