import discord
import config, time
import psutil as ps
from discord.ext import commands
from config import settings, emoji
from useful import prefix, copyright_ru, ping_list, bytes2human
startTime = time.time()
class Resource(commands.Cog):
    """Shows system information about the bot"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases = ['Analytics', 'analytics', 'Resources', 'resources', 'Resource', 'resource', 'Аналитика', 'аналитика', 'Загруженность', 'загруженность', 'Загруженностьбота', 'загруженностьбота', 'Загруженность_бота', 'загруженность_бота', 'Ресурсы', 'ресурсы', 'Ресурсыбота', 'ресурсыбота', 'Ресурсы_бота', 'ресурсы_бота'])
    async def __analytics(self, ctx):
        mem = ps.virtual_memory()
        ping = self.bot.ws.latency

        ping_emoji = emoji['ping_emoji']
        for ping_one in ping_list:
            if ping <= ping_one["ping"]:
                ping_emoji = ping_one["emoji"]
                break

        timeUp = time.time() - startTime
        hoursUp = round(timeUp) // 3600
        timeUp %= 3600
        minutesUp = round(timeUp) // 60
        timeUp = round(timeUp % 60)
        msg = "**{0}** час. **{1}** мин. **{2}** сек. назад :alarm_clock: ".format(hoursUp, minutesUp, timeUp)

        emb = discord.Embed(title = 'Загрузка бота')
        emb.add_field(name = 'Использование CPU', value = f'В настоящее время используется: {ps.cpu_percent()}%', inline = True)
        emb.add_field(name = 'Использование RAM', value = f'Доступно: {bytes2human(mem.available, "system")}\n' f'Используется: {bytes2human(mem.used, "system")} ({mem.percent}%)\n' f'Всего: {bytes2human(mem.total, "system")}', inline = True)
        emb.add_field(name = 'Пинг Бота', value = f'Пинг: {ping * 1000:.0f}ms\n'f'`{ping_emoji}`', inline = True)
        emb.add_field(name = 'Бот запустился:', value = msg, inline = True)
        emb.set_footer(text = copyright_ru, icon_url = self.bot.user.avatar_url)
        await ctx.send(embed = emb)
        print(f'[Logs:info] Информация о загрузке бота была выведена | {prefix}analytics')
def setup(bot):
    bot.add_cog(Resource(bot))