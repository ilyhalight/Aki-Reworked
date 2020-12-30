#*====Imports======
from logging import debug
import discord, os, datetime, sys, requests, pip, platform, getpass, aiohttp, shutil
from discord.ext import commands
from useful import settings, other, links, logcl, prefix
#*====Variables====
debugging = settings['debug']
make_backup = settings['backups']

owner_id = other['owner id']
cmd_count = other['commands']
patch = other['patch']

discordl = links['discord']

ConnectionMain = False

bot = commands.Bot(command_prefix = prefix)
bot.remove_command('help')

backup_status = 'Не сделан'
connection_status = 'Неизвестно'
#*====Functions====
def backup_dir():
    filename = 'backup'
    if os.path.isdir(filename):
        pass
    else:
        os.mkdir('backup')
        print('Папка для бэкапов была успешно создана')

def backup_test():
    global backup_status
    backup_dir()
    dt = datetime.datetime.now()
    data = dt.strftime("%Y-%m-%d-%H.%M.%S")
    dir_name = f'backup\\Aki {patch} {data}'
    os.makedirs(dir_name)
    os.makedirs(f'{dir_name}\\cogs')
    #os.makedirs(f'{dir_name}\\Localization')
    shutil.copy2('bot.py', f'{dir_name}')
    #shutil.copy2('config.py', f'{dir_name}') # TODO: Удалить, как закончу работу над переносом кфг системы
    shutil.copy2('config.json', f'{dir_name}')
    shutil.copy2('useful.py', f'{dir_name}')
    for file in os.listdir('.\\cogs'):
        if file.endswith('.py'):
            shutil.copy2(f'.\\cogs\\{file}', f'{dir_name}\\cogs')
    #for file in os.listdir('.\\Localization'):
    #    if file.endswith('.json'):
    #        shutil.copy2(f'.\\Localization\\{file}', f'{dir_name}\\Localization')
    backup_status = 'Сделан'

def connection_test(): # Узнаем, доступен ли discord.com
    global connection_status
    try:
        r = requests.get(discordl)
        if r.status_code != 200:
            connection_status = 'Отсутствует'
        if r.status_code == 200:
            connection_status = 'Успешное'
        else:
            connection_status = 'Неизвестно'
    except:
        connection_status = 'Неизвестно'

# Partially taken from Red-DiscordBot
def debug_info():

    if sys.platform == "linux":
        import distro

    IS_WINDOWS = os.name == 'nt'
    IS_MAC = sys.platform == 'darwin'
    IS_LINUX = sys.platform == 'linux'

    pyver = sys.version
    pipver = pip.__version__
    dispyver = discord.__version__
    akiver = other['patch']

    if IS_WINDOWS:
        os_info = platform.uname()
        osver = f'{os_info.system} {os_info.release} (version {os_info.version})'
    elif IS_MAC:
        os_info = platform.mac_ver()
        osver = f'Mac OS X {os_info[0]} {os_info[2]}'
    else:
        os_info = distro.linux_distribution()
        osver = f'{os_info[0]} {os_info[1]}'

    os_user = getpass.getuser()

    info = ('=====Debug info=====\n'
        + f'Aki version: {akiver}\n' # Версия aki
        + f'Python version: {pyver}\n' # Версия python
        + f'Python path: {sys.executable}\n' # Путь, куда установлен python
        + f'Pip version: {pipver}\n' # Версия pip
        + f'Discord.py version: {dispyver}\n' # Версия Discord.py
        + f'OS version: {osver}\n' # Версия ОС
        + f'Arch system: {platform.machine()}\n' # Битность
        + f'User: {os_user}\n' # Используемый пользователь
    )

    print(info)

def connection_ds():
    global connection_status # Отвечает за информацию о подключение к дискорду (В теории это показывает только подключено, Т.к при осутствии подключения к дискорду будет написано "Неизвестно")
    global ConnectionMain # TODO Передаем переменную, Чтобы узнать, не пытается ли бот запуститься второй раз (не работает)
    global backup_status # Сделан ли бекап, если сделан, будет написано "Успешно"

    if not ConnectionMain:
        connection_test()
        print('====Basic Config====') # Для красоты
        print(f'Подключение к Discord: {connection_status}') # Узнаем, доступен ли discord.com
        print(f'Префикс: "{prefix}"')
        print(f'Тег бота: {bot.user.name}#{bot.user.discriminator}')
        print(f'ID: {bot.user.id}')
        print(f'Всего команд: {cmd_count}')
        print(f'Бэкап: {backup_status}')
        print('====================\n') # Для красоты

        ConnectionMain = True
    else:
        print('Бот уже запущен')
#*=Error Functions=
def connection_ds_error():
    global connection_status # Отвечает за информацию о подключение к дискорду (В теории это показывает только подключено, Т.к при осутствии подключения к дискорду будет написано "Неизвестно")
    global ConnectionMain # TODO Передаем переменную, Чтобы узнать, не пытается ли бот запуститься второй раз (не работает)

    if not ConnectionMain:
        connection_test
        print('====Basic Config====') # Для красоты
        print(f'Подключение к Discord: {connection_status}') # Узнаем, доступен ли discord.com
        print(f'Префикс: "{prefix}"')
        print(f'Всего команд: {cmd_count}')
        print('====================\n') # Для красоты
#*====Events=======
@bot.event
async def on_ready():
    global debugging # Глобальная переменнеая дебагинг (Получаем из файла config.json)
    if make_backup: # Если истина делаем бекап
        backup_test()
    if debugging: # Если истина выводим дебаг информацию
        debug_info()
    connection_ds() # Выводим информацию о боте

@bot.event
async def on_guild_join(guild):
    emb = discord.Embed(color = logcl['guild join'], timestamp = datetime.datetime.now())
    for guild in bot.guilds:
        category = guild.categories[0]
        try:
            channel = category.text_channels[0]
        except:
            channel = category.voice_channels[0]
        chan = bot.get_channel(settings['log channel']) # айди канала для логов
        link = await channel.create_invite()
    emb.add_field( name = f'Бот зашёл на сервер\nСервер: `{guild.name}`\nID: `{guild.id}`', value = f'``Основатель: {guild.owner} \nID Основателя: {guild.owner_id} \nУчастников: {len(guild.members)} \nРегион: {guild.region} \nСоздан: {guild.created_at}`` \nСсылка: {link} \nСейчас бот поддерживает: {len(bot.guilds)} серверов')
    await chan.send(embed = emb)

@bot.event
async def on_guild_remove(guild):
    emb = discord.Embed(color = logcl['guild leave'], timestamp = datetime.datetime.now())
    for guild in bot.guilds:
        category = guild.categories[0]
        try:
            channel = category.text_channels[0]
        except:
            channel = category.voice_channels[0]
        chan = bot.get_channel(settings['log channel']) # айди канала для логов
        link = await channel.create_invite()
    emb.add_field( name = f'Бот покинул сервер\nСервер: `{guild.name}`\nID: `{guild.id}`', value = f'``Основатель: {guild.owner} \nID Основателя: {guild.owner_id} \nУчастников: {len(guild.members)} \nРегион: {guild.region} \nСоздан: {guild.created_at}`` \nСсылка: {link} \nСейчас бот поддерживает: {len(bot.guilds)} серверов')
    await chan.send(embed = emb)
#*====Commands=====
@bot.command(aliases = ['Load', 'load', 'Load_extension', 'load_extension', 'Load_extensions', 'load_extensions', 'Загрузить', 'загрузить', 'Загрузить_ког', 'загрузить_ког'])
async def __load(ctx, extensions):
    if ctx.author.id == owner_id: # Если автор команды = разработчику бота
        bot.load_extension(f'cogs.{extensions}') # Загружаем наш ког
        await ctx.send('Cogs is loaded...') # Ког загружен
    else:
        await ctx.send('Вы не разработчик бота...') # Вы не разработчик

@bot.command(aliases = ['Unload', 'unload', 'Unload_extension', 'unload_extension', 'Unload_extensions', 'unload_extensions', 'Отгрузить', 'отгрузить', 'Отгрузить_ког', 'отгрузить_ког'])
async def __unload(ctx, extensions):
    if ctx.author.id == owner_id: # Если автор команды = разработчику бота
        bot.unload_extension(f'cogs.{extensions}') # Выгружаем наш ког
        await ctx.send('Cogs is unloaded...') # Ког отгружен
    else:
        await ctx.send('Вы не разработчик бота...') # Вы не разработчик

@bot.command(aliases = ['Reload', 'reload', 'Reload_extension', 'reload_extension', 'Reload_extensions', 'reload_extensions', 'Перезагрузить', 'перезагрузить', 'Перезагрузить_ког', 'перезагрузить_ког'])
async def __reload(ctx, extensions):
    if ctx.author.id == owner_id: # Если автор команды = разработчику бота
        bot.unload_extension(f'cogs.{extensions}') # Перезапускаем ког
        bot.load_extension(f'cogs.{extensions}')
        await ctx.send('Cogs is restarted...') # Ког перезапущен
    else:
        await ctx.send('Вы не разработчик бота...') # Вы не разработчик

@bot.command(aliases = ['Backup', 'backup', 'Make_backup', 'make_backup', 'Бэкап', 'бэкап', 'Сделать_бэкап', 'сделать_бэкап', 'Резервное_копирование', 'резервное_копирование'])
async def __backup(ctx):
    if ctx.author.id == owner_id:
        try:
            backup_test()
            await ctx.send('Бэкап был успешно сделан.')
        except:
            await ctx.send('Произошла неизвестная ошибка!')
    else:
        await ctx.send('Ошибка! Вы не разработчик бота.')

# ! Читает коги только из папки cogs (подпапки не читаются!)
for file in os.listdir('./cogs'): # Цикл перебирающий файлы в cogs
    if file.endswith('.py'): # Если файл кончается на .py, то это наш ког
        bot.load_extension(f'cogs.{file[:-3]}') # Командуем боту загрузить все расширения.

#*====Bot Start====
try:
    bot.run (settings['token']) # Запуск бота
except aiohttp.ClientConnectorError:
    #connection_status == 'Отсутствует'
    connection_ds_error()