import discord
import datetime
from discord.ext import commands
from useful import links, defcl, diff, prefix, copyright_ru
class Time(commands.Cog):
    """Show the current time"""

    def __init__(self, bot):
        self.bot = bot
#c+p part
    @commands.command(aliases = ['Time', 'time', 'Clock', 'clock', 'Время', 'время', 'Часы', 'часы', 'Тайм', 'тайм'])
    async def __time(self, ctx):
        clock_dt = datetime.datetime.now()
        time_clock = (f"{clock_dt.hour}{clock_dt.minute}")
        time_clock = float(datetime.datetime.strptime(time_clock, '%H%M').strftime('%I.%M').lower())
        table_clock = diff
        result_clock = table_clock.get(time_clock, table_clock[min(table_clock.keys(), key = lambda k: abs(k-time_clock))])
        dt = datetime.datetime.now()
        data = (f'{dt.day}.{dt.month}.{dt.year}')
        time = (f'{dt.hour}:{dt.minute}')

        emb = discord.Embed(title = 'Время онлайн', description = 'Текущее время по МСК', colour = defcl['time'], url = links['time msc'])
        emb.set_footer(text = f'{copyright_ru}', icon_url = self.bot.user.avatar_url)
        emb.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
        emb.set_thumbnail(url = str(result_clock))
        emb.add_field(name = f'Дата: {data}', value = f'Время: {time}')
        await ctx.send(embed = emb)
        print(f'[Logs:utils] Часы были успешно выведены | {prefix}time')
def setup(bot):
    bot.add_cog(Time(bot))