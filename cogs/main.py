import discord
from discord.ext import commands
import os, config
from config import cogs_color, settings, quick_messages
prefix = settings['PREFIX']
class main(commands.Cog):
    
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Ready!')
        print(f'Logged in as ----> {self.client.user.name}')
        print(f'ID: {self.client.user.id}')
        await self.client.change_presence(status=discord.Status.idle, activity=discord.Streaming(name=f"Aki | Early Alpha", url="https://www.twitch.tv/bratishkinoff"))

def setup(client):
    client.add_cog(main(client))