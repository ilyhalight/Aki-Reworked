import discord
from discord.ext import commands
import config
from config import other_settings, fast_link
class main(commands.Cog):
    
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Ready!')
        print(f'Logged in as ----> {self.client.user.name}')
        print(f'ID: {self.client.user.id}')
        await self.client.change_presence(status = discord.Status.idle, activity = discord.Streaming(name = f'{self.client.user.name} | {other_settings["CURRENT VERSION"]}', url = fast_link['STREAM URL']))

def setup(client):
    client.add_cog(main(client))