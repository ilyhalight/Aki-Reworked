import discord
from discord.ext import commands
import os, config
from config import cogs_color, settings, quick_messages, other_settings
prefix = settings['PREFIX']
copyright_ru = quick_messages['COPYRIGHT RU']
copyright_en = quick_messages['COPYRIGHT EN']
com_value = other_settings['COMMAND VALUE']

class info(commands.Cog):
    
    def __init__(self, client):
        self.client = client

#   ███████╗███╗░░██╗░██████╗░██╗░░░░░██╗░██████╗██╗░░██╗
#   ██╔════╝████╗░██║██╔════╝░██║░░░░░██║██╔════╝██║░░██║
#   █████╗░░██╔██╗██║██║░░██╗░██║░░░░░██║╚█████╗░███████║
#   ██╔══╝░░██║╚████║██║░░╚██╗██║░░░░░██║░╚═══██╗██╔══██║
#   ███████╗██║░╚███║╚██████╔╝███████╗██║██████╔╝██║░░██║
#   ╚══════╝╚═╝░░╚══╝░╚═════╝░╚══════╝╚═╝╚═════╝░╚═╝░░╚═╝ 
    @commands.command(aliases = ['Help', 'help'])    
    async def __help(self, ctx, *, title = None):
        user = ctx.message.author
        if title == None:
            emb = discord.Embed(title = f'Available commands:', description = f'**Prefix: `{prefix}`**', color = cogs_color['HELP NONE COLOR'])
            emb.add_field(name = f'Information ({prefix}help Information)', value = f'`This section contains all information commands`', inline = False)
            emb.add_field(name = f'Moderation ({prefix}help Moderation)', value = f'`This section contains all the moderation commands`', inline = False)
            emb.add_field(name = f'Actions ({prefix}help Actions)', value = f'`This section contains all RP commands`', inline = False)
            emb.add_field(name = f'Funny ({prefix}help Funny)', value = f'`This section contains all the fun commands`', inline = False)
            emb.add_field(name = f'Utilities ({prefix}help Utilities)', value = f'`This section contains all the utilities`', inline = False)
            emb.add_field(name = f'Attention! If you notice errors or shortcomings, please describe it in the {prefix}bugs [NO WORK] command, we will be grateful!', value = f'Total commands: {com_value}', inline = False)
            emb.set_thumbnail(url = self.client.user.avatar_url)
            emb.set_footer(text = copyright_en, icon_url = self.client.user.avatar_url)
            await ctx.send (embed = emb)
            print(f'[Logs:info] Информация о категориях команд бота выведена для пользователя {user} | {prefix}help [EU]')
        if title != None:
            if title == 'Info' or title == 'info' or title == 'Information' or title == 'information':
                emb = discord.Embed(title = f'Available group commands: `Information`', description = f'**Prefix: `{prefix}`**', color = cogs_color['HELP NONE COLOR'])
                emb.add_field(name = f'{prefix}help', value = f'Help for all teams and their categories', inline = False)
                emb.add_field(name = f'{prefix}none', value = f'none', inline = False)
                emb.add_field(name = f'{prefix}none', value = f'none', inline = False)
                emb.add_field(name = f'{prefix}none', value = f'none', inline = False)
                emb.add_field(name = f'{prefix}none', value = f'none', inline = False)
                emb.add_field(name = f'Attention! If you notice errors or shortcomings, please describe it in the {prefix}bugs [NO WORK] command, we will be grateful!', value = f'Total commands: {com_value}', inline = False)
                emb.set_thumbnail(url = self.client.user.avatar_url)
                emb.set_footer(text = f'{copyright_en}', icon_url = self.client.user.avatar_url)
                await ctx.send (embed = emb)
                print(f'[Logs:info] Информация о категории "Информация" была выведена для пользователя {user} | {prefix}help info [EU]')      
            if title == 'Moderation' or title == 'moderation' or title == 'Moder' or title == 'moder':
                emb = discord.Embed(title = f'Available group commands: `Moderation`', description = f'**Prefix: `{prefix}`**', color = cogs_color['HELP NONE COLOR'])
                emb.add_field(name = f'{prefix}none', value = f'none', inline = False)
                emb.add_field(name = f'{prefix}none', value = f'none', inline = False)
                emb.add_field(name = f'{prefix}none', value = f'none', inline = False)
                emb.add_field(name = f'{prefix}none', value = f'none', inline = False)
                emb.add_field(name = f'{prefix}none', value = f'none', inline = False)
                emb.add_field(name = f'Attention! If you notice errors or shortcomings, please describe it in the {prefix}bugs [NO WORK] command, we will be grateful!', value = f'Total commands: {com_value}', inline = False)
                emb.set_thumbnail(url = self.client.user.avatar_url)
                emb.set_footer(text = copyright_en, icon_url = self.client.user.avatar_url)
                await ctx.send (embed = emb)
                print(f'[Logs:info] Информация о категории "Модерация" была выведена для пользователя {user} | {prefix}help moder [EU]')                              
            if title == 'Actions' or title == 'actions' or title == 'Action' or title == 'action':
                emb = discord.Embed(title = f'Available group commands: `Actions`', description = f'**Prefix: `{prefix}`**', color = cogs_color['HELP NONE COLOR'])
                emb.add_field(name = f'{prefix}none', value = f'none', inline = False)
                emb.add_field(name = f'{prefix}none', value = f'none', inline = False)
                emb.add_field(name = f'{prefix}none', value = f'none', inline = False)
                emb.add_field(name = f'{prefix}none', value = f'none', inline = False)
                emb.add_field(name = f'{prefix}none', value = f'none', inline = False)
                emb.add_field(name = f'Attention! If you notice errors or shortcomings, please describe it in the {prefix}bugs [NO WORK] command, we will be grateful!', value = f'Total commands: {com_value}', inline = False)
                emb.set_thumbnail(url = self.client.user.avatar_url)
                emb.set_footer(text = copyright_en, icon_url = self.client.user.avatar_url)
                await ctx.send (embed = emb)
                print(f'[Logs:info] Информация о категории "Действия" была выведена для пользователя {user} | {prefix}help moder [EU]')    
            if title == 'Funny' or title == 'funny' or title == 'Fun' or title == 'fun':
                emb = discord.Embed(title = f'Available group commands: `Funny`', description = f'**Prefix: `{prefix}`**', color = cogs_color['HELP NONE COLOR'])
                emb.add_field(name = f'{prefix}none', value = f'none', inline = False)
                emb.add_field(name = f'{prefix}none', value = f'none', inline = False)
                emb.add_field(name = f'{prefix}none', value = f'none', inline = False)
                emb.add_field(name = f'{prefix}none', value = f'none', inline = False)
                emb.add_field(name = f'{prefix}none', value = f'none', inline = False)
                emb.add_field(name = f'Attention! If you notice errors or shortcomings, please describe it in the {prefix}bugs [NO WORK] command, we will be grateful!', value = f'Total commands: {com_value}', inline = False)
                emb.set_thumbnail(url = self.client.user.avatar_url)
                emb.set_footer(text = copyright_en, icon_url = self.client.user.avatar_url)
                await ctx.send (embed = emb)
                print(f'[Logs:info] Информация о категории "Весёлое" была выведена для пользователя {user} | {prefix}help fun [EU]')    
            if title == 'Utilities' or title == 'utilities' or title == 'Util' or title == 'util':
                emb = discord.Embed(title = f'Available group commands: `Utilities`', description = f'**Prefix: `{prefix}`**', color = cogs_color['HELP NONE COLOR'])
                emb.add_field(name = f'{prefix}avatar', value = f'Show member avatar', inline = False)
                emb.add_field(name = f'{prefix}rand', value = f'Get a random number', inline = False)
                emb.add_field(name = f'{prefix}time', value = f'Shows the current time by CET', inline = False)
                emb.add_field(name = f'{prefix}wiki', value = f'Displays the information you are looking for from Wikipedia', inline = False)
                emb.add_field(name = f'{prefix}none', value = f'none', inline = False)
                emb.add_field(name = f'Attention! If you notice errors or shortcomings, please describe it in the {prefix}bugs [NO WORK] command, we will be grateful!', value = f'Total commands: {com_value}', inline = False)
                emb.set_thumbnail(url = self.client.user.avatar_url)
                emb.set_footer(text = copyright_en, icon_url = self.client.user.avatar_url)
                await ctx.send (embed = emb)
                print(f'[Logs:info] Информация о категории "Утилиты" была выведена для пользователя {user} | {prefix}help util [EU]')                

    @commands.command(aliases = ['Ahelp', 'ahelp', 'Admin_help', 'admin_help'])   
    @commands.is_owner() 
    async def __ahelp(self, ctx):     
            emb = discord.Embed(title = f'Available commands:', description = f'**Prefix: `{prefix}`**', color = cogs_color['AHELP COLOR'])
            emb.add_field(name = f'{prefix}test', value = f'Command for checking the bot`s health', inline = False)
            emb.add_field(name = f'{prefix}emoji', value = f'Add emoji to message', inline = False)
            emb.add_field(name = f'{prefix}del_emoji', value = f'Remove specific user emoji from a message', inline = False)
            emb.add_field(name = f'{prefix}clear_emoji', value = f'Remove all specific emojis from a message', inline = False)
            emb.add_field(name = f'{prefix}clear_all_emoji', value = f'Will remove absolutely all emoji from the message', inline = False)
            emb.add_field(name = f'{prefix}bot_status', value = f'Change bot status before reboot', inline = False)
            emb.set_thumbnail(url = self.client.user.avatar_url)
            emb.set_footer(text = copyright_en, icon_url = self.client.user.avatar_url)
            await ctx.send (embed = emb)
            print(f'[Logs:info] Админская сводка команд была выведена | {prefix}ahelp [EU]')                    

    @commands.command(aliases = ['Info', 'info', 'Bot', 'bot', 'Bot_info', 'bot_info'])
    async def __botinfo (self, ctx):
        emb = discord.Embed( title = ctx.guild.name, description = f'Bot information about the **{self.client.user.name}**.\n The bot was written specifically for the Fame Group project.\n More about commands - `{prefix}help`', colour = cogs_color['BOT INFO COLOR'])
        emb.add_field( name = f'Created me:', value = settings['OWNER'], inline=True)
        emb.add_field( name = f'Special thanks to:', value = settings['SPECIAL THANKS'], inline=True)
        emb.add_field( name = f'License:', value = 'CC CM-KD-QV', inline=True)
        emb.add_field( name = f'Version:', value = other_settings['CURRENT VERSION'], inline=True)
        emb.add_field( name = f'Patch:', value = other_settings['CURRENT PATCH'], inline=True)
        emb.set_thumbnail(url = self.client.user.avatar_url)
        emb.set_footer(text = copyright_en, icon_url = self.client.user.avatar_url)
        await ctx.send ( embed = emb)
        print(f"[Logs:info] Информация о боте была успешно выведена | {prefix}info [EN] ")         
        
    @commands.command(aliases = ['Server', 'server', 'Server_info', 'server_info']) # Thanks Fsoky community
    async def __serverinfo(self, ctx):
        allchannels = len(ctx.guild.channels)
        allvoice = len(ctx.guild.voice_channels)
        alltext = len(ctx.guild.text_channels)
        allroles = len(ctx.guild.roles)
        emb = discord.Embed(title=f"{ctx.guild.name}", color=cogs_color['SERVER INFO COLOR'], timestamp=ctx.message.created_at)
        emb.description=(
            f":timer: Server created: **{ctx.guild.created_at.strftime('%A, %b %#d %Y')}**\n\n"
            f":flag_white: Region: **{ctx.guild.region}\n\n:crown:Глава сервера **{ctx.guild.owner}**\n\n"
            f":shield: Verification level: **{ctx.guild.verification_level}**\n\n"
            f":musical_keyboard: Total channels: **{allchannels}**\n\n"
            f":loud_sound: Voice channels: **{allvoice}**\n\n"
            f":keyboard: Text channels: **{alltext}**\n\n"
            f":briefcase: Total roles: **{allroles}**\n\n"
            f":slight_smile: People on the server: **{ctx.guild.member_count}\n\n"
        )

        emb.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
        emb.set_thumbnail(url = self.client.user.avatar_url)
        emb.set_footer(text = copyright_en, icon_url = self.client.user.avatar_url)
        await ctx.send ( embed = emb)
        print(f"[Logs:info] Информация о сервере была успешно выведена | {prefix}server ")  
        
                       
#   ██████╗░██╗░░░██╗░██████╗░██████╗██╗░█████╗░███╗░░██╗
#   ██╔══██╗██║░░░██║██╔════╝██╔════╝██║██╔══██╗████╗░██║
#   ██████╔╝██║░░░██║╚█████╗░╚█████╗░██║███████║██╔██╗██║
#   ██╔══██╗██║░░░██║░╚═══██╗░╚═══██╗██║██╔══██║██║╚████║
#   ██║░░██║╚██████╔╝██████╔╝██████╔╝██║██║░░██║██║░╚███║
#   ╚═╝░░╚═╝░╚═════╝░╚═════╝░╚═════╝░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝    

    @commands.command(aliases = ['Хелп', 'хелп'])    
    async def ___help(self, ctx, *, title = None):
        user = ctx.message.author
        if title == None:
            emb = discord.Embed(title = f'Доступные команды:', description = f'**Префикс: `{prefix}`**', color = cogs_color['HELP NONE COLOR'])
            emb.add_field(name = f'Информация ({prefix}хелп Информация)', value = f'`В данном разделе содержатся все информационные команды`', inline = False)
            emb.add_field(name = f'Модерация ({prefix}хелп Модерация)', value = f'`В данном разделе содержатся все команды модерации`', inline = False)
            emb.add_field(name = f'Действия ({prefix}хелп Действия)', value = f'`В данном разделе содержатся все РП команды`', inline = False)
            emb.add_field(name = f'Весёлое ({prefix}хелп Весёлое)', value = f'`В данном разделе содержатся все весёлые команды`', inline = False)
            emb.add_field(name = f'Утилиты ({prefix}хелп Утилиты)', value = f'`В данном разделе содержатся все утилиты`', inline = False)
            emb.add_field(name = f'Внимание! Если заметили ошибки или недочёты, пожалуйста, опишите её в команде {prefix}bugs [NO WORK], будем благодарны!', value = f'Всего команд: {com_value}', inline = False)
            emb.set_thumbnail(url = self.client.user.avatar_url)
            emb.set_footer(text = copyright_ru, icon_url = self.client.user.avatar_url)
            await ctx.send (embed = emb)
            print(f'[Logs:info] Информация о категориях команд бота была выведена для пользователя {user} | {prefix}хелп [RU]')
        if title != None:
            if title == 'Инфо' or title == 'инфо' or title == 'Информация' or title == 'информация':
                emb = discord.Embed(title = f'Доступные команды группы: `Информация`', description = f'**Префикс: `{prefix}`**', color = cogs_color['HELP NONE COLOR'])
                emb.add_field(name = f'{prefix}хелп', value = f'Справка по всем команда и их категориям', inline = False)
                emb.add_field(name = f'{prefix}none', value = f'none', inline = False)
                emb.add_field(name = f'{prefix}none', value = f'none', inline = False)
                emb.add_field(name = f'{prefix}none', value = f'none', inline = False)
                emb.add_field(name = f'{prefix}none', value = f'none', inline = False)
                emb.add_field(name = f'Внимание! Если заметили ошибки или недочёты, пожалуйста, опишите её в команде {prefix}bugs [NO WORK], будем благодарны!', value = f'Всего команд: {com_value}', inline = False)
                emb.set_thumbnail(url = self.client.user.avatar_url)
                emb.set_footer(text = copyright_ru, icon_url = self.client.user.avatar_url)
                await ctx.send (embed = emb)    
                print(f'[Logs:info] Информация о категории "Информация" была выведена для пользователя {user} | {prefix}хелп инфо [RU]')   
            if title == 'Модерирование' or title == 'модерирование' or title == 'Модер' or title == 'модер' or title == 'Модерация' or title == 'модерация':
                emb = discord.Embed(title = f'Доступные команды группы: `Модерация`', description = f'**Префикс: `{prefix}`**', color = cogs_color['HELP NONE COLOR'])
                emb.add_field(name = f'{prefix}none', value = f'none', inline = False)
                emb.add_field(name = f'{prefix}none', value = f'none', inline = False)
                emb.add_field(name = f'{prefix}none', value = f'none', inline = False)
                emb.add_field(name = f'{prefix}none', value = f'none', inline = False)
                emb.add_field(name = f'{prefix}none', value = f'none', inline = False)
                emb.add_field(name = f'Внимание! Если заметили ошибки или недочёты, пожалуйста, опишите её в команде {prefix}bugs [NO WORK], будем благодарны!', value = f'Всего команд: {com_value}', inline = False)
                emb.set_thumbnail(url = self.client.user.avatar_url)
                emb.set_footer(text = copyright_ru, icon_url = self.client.user.avatar_url)
                await ctx.send (embed = emb)    
                print(f'[Logs:info] Информация о категории "Модерация" была выведена для пользователя {user} | {prefix}хелп модер [RU]')
            if title == 'Действия' or title == 'действия':
                emb = discord.Embed(title = f'Доступные команды группы: `Действия`', description = f'**Префикс: `{prefix}`**', color = cogs_color['HELP NONE COLOR'])
                emb.add_field(name = f'{prefix}none', value = f'none', inline = False)
                emb.add_field(name = f'{prefix}none', value = f'none', inline = False)
                emb.add_field(name = f'{prefix}none', value = f'none', inline = False)
                emb.add_field(name = f'{prefix}none', value = f'none', inline = False)
                emb.add_field(name = f'{prefix}none', value = f'none', inline = False)
                emb.add_field(name = f'Внимание! Если заметили ошибки или недочёты, пожалуйста, опишите её в команде {prefix}bugs [NO WORK], будем благодарны!', value = f'Всего команд: {com_value}', inline = False)
                emb.set_thumbnail(url = self.client.user.avatar_url)
                emb.set_footer(text =copyright_ru, icon_url = self.client.user.avatar_url)
                await ctx.send (embed = emb)    
                print(f'[Logs:info] Информация о категории "Действия" была выведена для пользователя {user} | {prefix}хелп действия [RU]')                                      
            if title == 'Весёлое' or title == 'весёлое':
                emb = discord.Embed(title = f'Доступные команды группы: `Весёлое`', description = f'**Префикс: `{prefix}`**', color = cogs_color['HELP NONE COLOR'])
                emb.add_field(name = f'{prefix}none', value = f'none', inline = False)
                emb.add_field(name = f'{prefix}none', value = f'none', inline = False)
                emb.add_field(name = f'{prefix}none', value = f'none', inline = False)
                emb.add_field(name = f'{prefix}none', value = f'none', inline = False)
                emb.add_field(name = f'{prefix}none', value = f'none', inline = False)
                emb.add_field(name = f'Внимание! Если заметили ошибки или недочёты, пожалуйста, опишите её в команде {prefix}bugs [NO WORK], будем благодарны!', value = f'Всего команд: {com_value}', inline = False)
                emb.set_thumbnail(url = self.client.user.avatar_url)
                emb.set_footer(text = copyright_ru, icon_url = self.client.user.avatar_url)
                await ctx.send (embed = emb)    
                print(f'[Logs:info] Информация о категории "Весёлое" была выведена для пользователя {user} | {prefix}хелп весёлое [RU]')   
            if title == 'Утилиты' or title == 'утилиты' or title == 'Утил' or title == 'утил':
                emb = discord.Embed(title = f'Доступные команды группы: `Утилиты`', description = f'**Префикс: `{prefix}`**', color = cogs_color['HELP NONE COLOR'])
                emb.add_field(name = f'{prefix}аватар', value = f'Показать аватар участника', inline = False)
                emb.add_field(name = f'{prefix}ранд', value = f'Получить рандомное число', inline = False)
                emb.add_field(name = f'{prefix}тайм', value = f'Показывает текущее время по МСК', inline = False)
                emb.add_field(name = f'{prefix}вики', value = f'Выводит искомую информацию с википедии', inline = False)
                emb.add_field(name = f'{prefix}none', value = f'none', inline = False)
                emb.add_field(name = f'Внимание! Если заметили ошибки или недочёты, пожалуйста, опишите её в команде {prefix}bugs [NO WORK], будем благодарны!', value = f'Всего команд: {com_value}', inline = False)
                emb.set_thumbnail(url = self.client.user.avatar_url)
                emb.set_footer(text = copyright_ru, icon_url = self.client.user.avatar_url)
                await ctx.send (embed = emb)    
                print(f'[Logs:info] Информация о категории "Утилиты" была выведена для пользователя {user} | {prefix}хелп утилиты [RU]')      
                            
    @commands.command(aliases = ['Ахелп', 'ахелп', 'Админ_хелп', 'админ_хелп'])   
    @commands.is_owner() 
    async def ___ahelp(self, ctx):     
            emb = discord.Embed(title = f'Доступные команды:', description = f'**Префикс: `{prefix}`**', color = cogs_color['AHELP COLOR'])
            emb.add_field(name = f'{prefix}тест', value = f'Команда для проверки работоспособности бота', inline = False)
            emb.add_field(name = f'{prefix}эмоджи', value = f'Добавить эмоджи к сообщению', inline = False)
            emb.add_field(name = f'{prefix}удалить_эмоджи', value = f'Удалить конкретные эмоджи пользователя с сообщения', inline = False)
            emb.add_field(name = f'{prefix}стереть_эмодзи', value = f'Стереть конкретные эмоджи с сообщения', inline = False)
            emb.add_field(name = f'{prefix}стереть_все_эмодзи', value = f'Стереть абсолютно все эмоджи с сообщения', inline = False)
            emb.add_field(name = f'{prefix}бот_статус', value = f'Изменить статус бота до перезагрузки', inline = False)
            emb.set_thumbnail(url = self.client.user.avatar_url)
            emb.set_footer(text = copyright_ru, icon_url = self.client.user.avatar_url)
            await ctx.send (embed = emb)
            print(f'[Logs:info] Админская сводка команд была выведена | {prefix}ахелп [RU]')   

    @commands.command(aliases = ['Инфо', 'инфо', 'Бот', 'бот', 'Бот_инфо', 'бот_инфо'])
    async def ___botinfo (self, ctx):
        emb = discord.Embed( title = ctx.guild.name, description = f'Информация о боте **{self.client.user.name}**.\n Бот был написан специально для проекта Fame Group.\n Подробнее о командах - `{prefix}хелп`', colour = cogs_color['BOT INFO COLOR'])
        emb.add_field( name = f'Меня создал:', value = settings['OWNER'], inline=True)
        emb.add_field( name = f'Отдельное спасибо:', value = settings['SPECIAL THANKS'], inline=True)
        emb.add_field( name = f'Лицензия:', value = 'CC CM-KD-QV', inline=True)
        emb.add_field( name = f'Версия:', value = other_settings['CURRENT VERSION'], inline=True)
        emb.add_field( name = f'Патч:', value = other_settings['CURRENT PATCH'], inline=True)
        emb.set_thumbnail(url = self.client.user.avatar_url)
        emb.set_footer(text = copyright_ru, icon_url = self.client.user.avatar_url)
        await ctx.send ( embed = emb)
        print(f"[Logs:info] Информация о боте была успешно выведена | {prefix}инфо [RU]")   
    
    @commands.command(aliases = ['Сервер', 'сервер', 'Сервер_инфо', 'сервер_инфо']) # Thanks Fsoky community
    async def ___serverinfo(self, ctx):
        allchannels = len(ctx.guild.channels)
        allvoice = len(ctx.guild.voice_channels)
        alltext = len(ctx.guild.text_channels)
        allroles = len(ctx.guild.roles)
        emb = discord.Embed(title=ctx.guild.name, color=cogs_color['SERVER INFO COLOR'], timestamp=ctx.message.created_at)
        emb.description=(
            f":timer: Сервер создали: **{ctx.guild.created_at.strftime('%A, %b %#d %Y')}**\n\n"
            f":flag_white: Регион: **{ctx.guild.region}\n\n:crown:Глава сервера **{ctx.guild.owner}**\n\n"
            f":shield: Уровень верификации: **{ctx.guild.verification_level}**\n\n"
            f":musical_keyboard: Всего каналов: **{allchannels}**\n\n"
            f":loud_sound: Голосовых каналов: **{allvoice}**\n\n"
            f":keyboard: Текстовых каналов: **{alltext}**\n\n"
            f":briefcase: Всего ролей: **{allroles}**\n\n"
            f":slight_smile: Людей на сервере: **{ctx.guild.member_count}\n\n"
        )

        emb.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
        emb.set_thumbnail(url = self.client.user.avatar_url)
        emb.set_footer(text = copyright_ru, icon_url = self.client.user.avatar_url)
        await ctx.send ( embed = emb)
        print(f"[Logs:info] Информация о сервере была успешно выведена | {prefix}server ")          
                
def setup(client):
    client.add_cog(info(client))