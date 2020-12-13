import discord
import config, datetime, pytz, useful
from discord.ext import commands
from config import cogs_color, fast_link
from useful import diff, prefix, copyright_en
class Time(commands.Cog):
    """Show the current time"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases = ['Time', 'time', 'Clock', 'clock', 'Время', 'время', 'Часы', 'часы', 'Тайм', 'тайм'])
    async def __time(self, ctx):
#_________main code_________
        tz_paris = pytz.timezone('Europe/Paris')
        clock_dt = datetime.datetime.now(tz_paris)
        time_clock = (f"{clock_dt.hour}{clock_dt.minute}")
        time_clock = float(datetime.datetime.strptime(time_clock, '%H%M').strftime('%I.%M').lower())
        table_clock = diff
        result_clock = table_clock.get(time_clock, table_clock[min(table_clock.keys(), key=lambda k: abs(k-time_clock))])
        dt = datetime.datetime.now(tz_paris)
        data = (f'{dt.day}.{dt.month}.{dt.year}')
        time = (f'{dt.hour}:{dt.minute}')
#_________embeds____________
        emb = discord.Embed( title = 'Online time', description = 'Current time by CET', colour = cogs_color['TIME COLOR'], url = fast_link['TIME CET'])
        emb.set_footer(text = f'{copyright_en}', icon_url = self.bot.user.avatar_url)
        emb.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
        emb.set_thumbnail(url = str(result_clock))
        emb.add_field(name = f'Date: {data}', value = f'Time: {time}')
        await ctx.send(embed = emb)
        print(f'[Logs:utils] Часы были успешно выведены | {prefix}time')
def setup(bot):
    bot.add_cog(Time(bot))