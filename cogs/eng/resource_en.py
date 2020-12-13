import discord
import config, time
import psutil as ps
from discord.ext import commands
from config import settings, emoji
from useful import prefix, copyright_en, ping_list, bytes2human
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
        msg = '**{0}** hour. **{1}** min. **{2}** sec. ago :alarm_clock: '.format(hoursUp, minutesUp, timeUp)

        emb = discord.Embed(title = 'Загрузка бота')
        emb.add_field(name = 'CPU usage', value = f'Currently in use: {ps.cpu_percent()}%', inline = True)
        emb.add_field(name = 'RAM usag', value = f'Available: {bytes2human(mem.available, "system")}\n' f'Used: {bytes2human(mem.used, "system")} ({mem.percent}%)\n' f'Total: {bytes2human(mem.total, "system")}', inline = True)
        emb.add_field(name = 'Bot Ping', value = f'Ping: {ping * 1000:.0f}ms\n'f'`{ping_emoji}`', inline = True)
        emb.add_field(name = 'Bot started:', value = msg, inline = True)
        emb.set_footer(text = copyright_en, icon_url = self.bot.user.avatar_url)
        await ctx.send(embed = emb)
        print(f'[Logs:info] Информация о загрузке бота была выведена | {prefix}analytics')
def setup(bot):
    bot.add_cog(Resource(bot))