import discord
from discord.ext import commands
import config
from config import other_settings, fast_link
from useful import prefix
class Status(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        await self.bot.change_presence(status = discord.Status.idle, activity = discord.Streaming(name = f'{prefix}help | {other_settings["CURRENT VERSION"]}', url = fast_link['STREAM URL']))

def setup(bot):
    bot.add_cog(Status(bot)) # Добавляем в список когов