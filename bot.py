#_________imports___________
import discord
import os, datetime, config
from discord.ext import commands
from config import settings, other_settings, channels, cogs_color
#_________variables_________
prefix = settings['PREFIX']
bot = commands.Bot(command_prefix = prefix)
bot.remove_command('help')
owner_id = settings['OWNER ID']
bot_id = settings['ID']
command_count = other_settings['COMMAND VALUE']
ConnectionMain = False
#_________events____________
@bot.event
async def on_ready():
    global ConnectionMain # Глобальная переменная ConnectionMain

    if not ConnectionMain:
        print('____________________') # Для красоты
        print('Успешное подключение к Discord')
        print(f'Префикс: "{prefix}"')
        print(f'Тег бота: {bot.user.name}#{bot.user.discriminator}')
        print(f'ID: {bot_id}')
        print(f'Всего команд: {command_count}')
        print("____________________\n") # Для красоты

        ConnectionMain = True

    else:
        print('\n____________________') # Для красоты
        print('[Error:event] Ивент on_ready сработал ещё раз!')
        print('____________________\n') # Для красоты

@bot.event
async def on_guild_join(guild):
    emb = discord.Embed(color = cogs_color['ON GUILD JOIN LOG'], timestamp = datetime.datetime.now())
    for guild in bot.guilds:
        category = guild.categories[0]
        try:
            channel = category.text_channels[0]
        except:
            channel = category.voice_channels[0]
        chan = bot.get_channel(channels['LOG JOIN CHANNEL']) # айди канала для логов
        link = await channel.create_invite()
    emb.add_field( name = f'Бот зашёл на сервер\nСервер: `{guild.name}`\nID: `{guild.id}`', value = f'``Основатель: {guild.owner} \nID Основателя: {guild.owner_id} \nУчастников: {len(guild.members)} \nРегион: {guild.region} \nСоздан: {guild.created_at}`` \nСсылка: {link} \nСейчас бот поддерживает: {len(bot.guilds)} серверов')
    await chan.send(embed=emb)

@bot.event
async def on_guild_remove(guild):
    emb = discord.Embed(color = cogs_color['ON GUILD LEAVE LOG'], timestamp = datetime.datetime.now())
    for guild in bot.guilds:
        category = guild.categories[0]
        try:
            channel = category.text_channels[0]
        except:
            channel = category.voice_channels[0]
        chan = bot.get_channel(channels['LOG LEAVE CHANNEL']) # айди канала для логов
        link = await channel.create_invite()
    emb.add_field( name = f'Бот покинул сервер\nСервер: `{guild.name}`\nID: `{guild.id}`', value = f'``Основатель: {guild.owner} \nID Основателя: {guild.owner_id} \nУчастников: {len(guild.members)} \nРегион: {guild.region} \nСоздан: {guild.created_at}`` \nСсылка: {link} \nСейчас бот поддерживает: {len(bot.guilds)} серверов')
    await chan.send(embed=emb)
#_________commands__________
@bot.command()
async def load(ctx, extensions):
    if ctx.author.id == owner_id: # Если автор команды = разработчику бота
        bot.load_extension(f'cogs.{extensions}') # Загружаем наш ког
        await ctx.send('Cogs is loaded...') # Ког загружен
    else:
        await ctx.send('Вы не разработчик бота...') # Вы не разработчик

@bot.command()
async def unload(ctx, extensions):
    if ctx.author.id == owner_id: # Если автор команды = разработчику бота
        bot.unload_extension(f'cogs.{extensions}') # Выгружаем наш ког
        await ctx.send('Cogs is unloaded...') # Ког отгружен
    else:
        await ctx.send('Вы не разработчик бота...') # Вы не разработчик

@bot.command()
async def reload(ctx, extensions):
    if ctx.author.id == owner_id: # Если автор команды = разработчику бота
        bot.unload_extension(f'cogs.{extensions}') # Перезапускаем ког
        bot.load_extension(f'cogs.{extensions}')
        await ctx.send('Cogs is restarted...') # Ког перезапущен
    else:
        await ctx.send('Вы не разработчик бота...') # Вы не разработчик

print(f'Загруженные коги: ')
for file in os.listdir('./cogs'): # Цикл перебирающий файлы в cogs

    if file.endswith('.py'): # Если файл кончается на .py, то это наш ког
        bot.load_extension(f'cogs.{file[:-3]}') # Командуем боту загрузить все расширения.
        print(f'    {file[:-3]}') # Выводим список всех наших когов

#_________bot starting______
bot.run (settings['TOKEN']) # Запуск бота