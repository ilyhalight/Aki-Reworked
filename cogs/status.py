import discord
from discord.ext import commands
from useful import links, other, prefix
class Status(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        await self.bot.change_presence(status = discord.Status.idle, activity = discord.Streaming(name = f'{prefix}help | {other["version"]}', url = links['stream']))

def setup(bot):
    bot.add_cog(Status(bot)) # Добавляем в список когов