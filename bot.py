import discord
import os
from discord.ext import commands
import config
from config import cogs_color,  settings
prefix = settings['PREFIX']
client = commands.Bot(command_prefix=prefix)
client.remove_command('help')
owner_id = settings['OWNER ID']
@client.command()
async def load(ctx, extensions):
    if ctx.author.id == owner_id:
        client.load_extension(f'cogs.{extensions}')
        await ctx.send('Cogs is loaded...')
    else:
        await ctx.send('Вы не разработчик бота...')
        
@client.command()
async def unload(ctx, extensions):
    if ctx.author.id == owner_id:
        client.unload_extension(f'cogs.{extensions}')
        await ctx.send('Cogs is unloaded...')
    else:
        await ctx.send('Вы не разработчик бота...')
        
@client.command()
async def reload(ctx, extensions):
    if ctx.author.id == owner_id:
        client.unload_extension(f'cogs.{extensions}')
        client.load_extension(f'cogs.{extensions}')
        await ctx.send('Cogs is restarted...')
    else:
        await ctx.send('Вы не разработчик бота...')
        
for filename in os.listdir('./cogs'): # Цикл перебирающий файлы в cogs
    if filename.endswith('.py'): # еTсли файл кончается на .py, то это наш ког
        client.load_extension(f'cogs.{filename[:-3]}') #командуем боту загрузить все расширения.
        
client.run (settings['TOKEN'])
