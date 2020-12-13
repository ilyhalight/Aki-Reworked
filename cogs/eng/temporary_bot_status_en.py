import discord
import config
from discord.ext import commands
from config import cogs_color, quick_messages, fast_link
from useful import prefix, copyright_en
status_log = quick_messages['BOT STATUS LOG']
unknown_log = quick_messages['UNKNOWN ERROR LOG']
unknown = quick_messages['UNKNOWN ERROR EN']
class Temporary_bot_status(commands.Cog):
    """Sets a temporary status for the bot"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases = ['Temporary_bot_status', 'temporary_bot_status', 'Temp_bot_status', 'temp_bot_status', 'Временный_статус_бота', 'временный_статус_бота'])
    @commands.is_owner()
    async def __botstatus(self, ctx, active = None, *, arg = None):
        if active == None or arg == None:
            emb = discord.Embed(description = f'Example: `{prefix}Temporary_bot_status Stream $help` - The temporary bot status will be changed to: "Stream $help".', color = cogs_color['BOT COLOR EXAMPLE'])
            emb.set_footer(text = copyright_en, icon_url = self.bot.user.avatar_url)
            await ctx.send(embed = emb)
            print(f'[Logs:error] Один из аргументов не был введен корректно | {prefix}Temp_bot_status')

        if arg != None:
            if active == 'Listening' or active == 'listening' or active == 'Listen' or active == 'listen' or active == 'Слушает' or active == 'слушает' or active == 'Слушать' or active == 'слушать':
                await self.bot.change_presence(status = discord.Status.idle, activity = discord.Activity(name = arg, type = discord.ActivityType.listening))
                await ctx.send('Changing...')
                print(f'{status_log} "Слушает {arg}" | {prefix}Temp_bot_status')

            if active == 'Playing' or active == 'playing' or active == 'Play' or active == 'play' or active == 'Играет' or active == 'играет' or active == 'Игра' or active == 'игра' or active == 'Играть' or active == 'играть':
                await self.bot.change_presence(status = discord.Status.idle, activity = discord.Activity(name = arg, type = discord.ActivityType.streaming))
                await ctx.send('Changing...')
                print(f'{status_log} "Играет в {arg}" | {prefix}Temp_bot_status')

            if active == 'Streaming' or active == 'streaming' or active == 'Stream' or active == 'stream' or active == 'Стримит' or active == 'стримит' or active == 'Стрим' or active == 'стрим' or active == 'Стримить' or active == 'стримить':
                await self.bot.change_presence(status = discord.Status.idle, activity = discord.Activity(name = arg, url = fast_link['STREAM URL'], type = discord.ActivityType.streaming))
                await ctx.send('Changing...')
                print(f'{status_log} "Стримит {arg}" | {prefix}Temp_bot_status')

            if active == 'Watching' or active == 'watching' or active == 'Watch' or active == 'watch' or active == 'Смотрит' or active == 'смотрит' or active == 'Смотреть' or active == 'смотреть':
                await self.bot.change_presence(status = discord.Status.idle, activity = discord.Activity(name = arg, type = discord.ActivityType.watching))
                await ctx.send('Changing...')
                print(f'{status_log} "Смотрит {arg}" | {prefix}Temp_bot_status')

            else:
                emb = discord.Embed(description = unknown, color = cogs_color['BOT COLOR ERROR'])
                emb.set_footer(text = copyright_en, icon_url = self.bot.user.avatar_url)
                await ctx.send(embed = emb)
                print(f'{unknown_log} {prefix}Temp_bot_status')
def setup(bot):
    bot.add_cog(Temporary_bot_status(bot))