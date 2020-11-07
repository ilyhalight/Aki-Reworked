import discord
from discord.ext import commands
import os, config
from config import cogs_color, settings, quick_messages, other_settings
prefix = settings['PREFIX']
unknown_log = quick_messages['UNKNOWN ERROR LOG']
unknown = quick_messages['UNKNOWN ERROR']
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
            emb.add_field(name = f'Information ({prefix}help Information)', value = f'`This section contains all information commands`', inline=False)
            emb.add_field(name = f'Moderation ({prefix}help Moderation)', value = f'`This section contains all the moderation commands`', inline=False)
            emb.add_field(name = f'Actions ({prefix}help Actions)', value = f'`This section contains all RP commands`', inline=False)
            emb.add_field(name = f'Funny ({prefix}help Funny)', value = f'`This section contains all the fun commands`', inline=False)
            emb.add_field(name = f'Utilities ({prefix}help Utilities)', value = f'`This section contains all the utilities`', inline=False)
            emb.add_field(name = f'Attention! If you notice errors or shortcomings, please describe it in the {prefix} bugs [NO WORK] command, we will be grateful!', value = f'Total commands: {com_value}', inline=False)
            emb.set_thumbnail(url = self.client.user.avatar_url)
            emb.set_footer(text = f'{copyright_en}', icon_url = self.client.user.avatar_url)
            await ctx.send (embed = emb)
            print(f'[Logs:info] Информация о категориях команд бота выведена для пользователя {user} | {prefix}help [EU]')
        if title != None:
            if title == 'Info' or title == 'info' or title == 'Information' or title == 'information':
                emb = discord.Embed(title = f'Available group commands: `Information`', description = f'**Prefix: `{prefix}`**', color = cogs_color['HELP NONE COLOR'])
                emb.add_field(name = f'{prefix}help', value = f'Help for all teams and their categories', inline=False)
                emb.add_field(name = f'{prefix}none', value = f'none', inline=False)
                emb.add_field(name = f'{prefix}none', value = f'none', inline=False)
                emb.add_field(name = f'{prefix}none', value = f'none', inline=False)
                emb.add_field(name = f'{prefix}none', value = f'none', inline=False)
                emb.add_field(name = f'Attention! If you notice errors or shortcomings, please describe it in the {prefix} bugs [NO WORK] command, we will be grateful!', value = f'Total commands: {com_value}', inline=False)
                emb.set_thumbnail(url = self.client.user.avatar_url)
                emb.set_footer(text = f'{copyright_en}', icon_url = self.client.user.avatar_url)
                await ctx.send (embed = emb)
                print(f'[Logs:info] Информация о категории "Информация" была выведена для пользователя {user} | {prefix}help info [EU]')      
            if title == 'Moderation' or title == 'moderation' or title == 'Moder' or title == 'moder':
                emb = discord.Embed(title = f'Available group commands: `Moderation`', description = f'**Prefix: `{prefix}`**', color = cogs_color['HELP NONE COLOR'])
                emb.add_field(name = f'{prefix}none', value = f'none', inline=False)
                emb.add_field(name = f'{prefix}none', value = f'none', inline=False)
                emb.add_field(name = f'{prefix}none', value = f'none', inline=False)
                emb.add_field(name = f'{prefix}none', value = f'none', inline=False)
                emb.add_field(name = f'{prefix}none', value = f'none', inline=False)
                emb.add_field(name = f'Attention! If you notice errors or shortcomings, please describe it in the {prefix} bugs [NO WORK] command, we will be grateful!', value = f'Total commands: {com_value}', inline=False)
                emb.set_thumbnail(url = self.client.user.avatar_url)
                emb.set_footer(text = f'{copyright_en}', icon_url = self.client.user.avatar_url)
                await ctx.send (embed = emb)
                print(f'[Logs:info] Информация о категории "Модерация" была выведена для пользователя {user} | {prefix}help moder [EU]')                              
            if title == 'Actions' or title == 'actions' or title == 'Action' or title == 'action':
                emb = discord.Embed(title = f'Available group commands: `Actions`', description = f'**Prefix: `{prefix}`**', color = cogs_color['HELP NONE COLOR'])
                emb.add_field(name = f'{prefix}none', value = f'none', inline=False)
                emb.add_field(name = f'{prefix}none', value = f'none', inline=False)
                emb.add_field(name = f'{prefix}none', value = f'none', inline=False)
                emb.add_field(name = f'{prefix}none', value = f'none', inline=False)
                emb.add_field(name = f'{prefix}none', value = f'none', inline=False)
                emb.add_field(name = f'Attention! If you notice errors or shortcomings, please describe it in the {prefix} bugs [NO WORK] command, we will be grateful!', value = f'Total commands: {com_value}', inline=False)
                emb.set_thumbnail(url = self.client.user.avatar_url)
                emb.set_footer(text = f'{copyright_en}', icon_url = self.client.user.avatar_url)
                await ctx.send (embed = emb)
                print(f'[Logs:info] Информация о категории "Действия" была выведена для пользователя {user} | {prefix}help moder [EU]')    
            if title == 'Funny' or title == 'funny' or title == 'Fun' or title == 'fun':
                emb = discord.Embed(title = f'Available group commands: `Funny`', description = f'**Prefix: `{prefix}`**', color = cogs_color['HELP NONE COLOR'])
                emb.add_field(name = f'{prefix}none', value = f'none', inline=False)
                emb.add_field(name = f'{prefix}none', value = f'none', inline=False)
                emb.add_field(name = f'{prefix}none', value = f'none', inline=False)
                emb.add_field(name = f'{prefix}none', value = f'none', inline=False)
                emb.add_field(name = f'{prefix}none', value = f'none', inline=False)
                emb.add_field(name = f'Attention! If you notice errors or shortcomings, please describe it in the {prefix} bugs [NO WORK] command, we will be grateful!', value = f'Total commands: {com_value}', inline=False)
                emb.set_thumbnail(url = self.client.user.avatar_url)
                emb.set_footer(text = f'{copyright_en}', icon_url = self.client.user.avatar_url)
                await ctx.send (embed = emb)
                print(f'[Logs:info] Информация о категории "Весёлое" была выведена для пользователя {user} | {prefix}help fun [EU]')    
            if title == 'Utilities' or title == 'utilities' or title == 'Util' or title == 'util':
                emb = discord.Embed(title = f'Available group commands: `Utilities`', description = f'**Prefix: `{prefix}`**', color = cogs_color['HELP NONE COLOR'])
                emb.add_field(name = f'{prefix}avatar', value = f'Show member avatar', inline=False)
                emb.add_field(name = f'{prefix}rand', value = f'Get a random number', inline=False)
                emb.add_field(name = f'{prefix}time', value = f'Shows the current time by CET', inline=False)
                emb.add_field(name = f'{prefix}wiki', value = f'Displays the information you are looking for from Wikipedia', inline=False)
                emb.add_field(name = f'{prefix}none', value = f'none', inline=False)
                emb.add_field(name = f'Attention! If you notice errors or shortcomings, please describe it in the {prefix} bugs [NO WORK] command, we will be grateful!', value = f'Total commands: {com_value}', inline=False)
                emb.set_thumbnail(url = self.client.user.avatar_url)
                emb.set_footer(text = f'{copyright_en}', icon_url = self.client.user.avatar_url)
                await ctx.send (embed = emb)
                print(f'[Logs:info] Информация о категории "Утилиты" была выведена для пользователя {user} | {prefix}help util [EU]')                
                
                
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
            emb.add_field(name = f'Информация ({prefix}хелп Информация)', value = f'`В данном разделе содержатся все информационные команды`', inline=False)
            emb.add_field(name = f'Модерация ({prefix}хелп Модерация)', value = f'`В данном разделе содержатся все команды модерации`', inline=False)
            emb.add_field(name = f'Действия ({prefix}хелп Действия)', value = f'`В данном разделе содержатся все РП команды`', inline=False)
            emb.add_field(name = f'Весёлое ({prefix}хелп Весёлое)', value = f'`В данном разделе содержатся все весёлые команды`', inline=False)
            emb.add_field(name = f'Утилиты ({prefix}хелп Утилиты)', value = f'`В данном разделе содержатся все утилиты`', inline=False)
            emb.add_field(name = f'Внимание! Если заметили ошибки или недочёты, пожалуйста, опишите её в команде {prefix}bugs [NO WORK], будем благодарны!', value = f'Всего команд: {com_value}', inline=False)
            emb.set_thumbnail(url = self.client.user.avatar_url)
            emb.set_footer(text = f'{copyright_en}', icon_url = self.client.user.avatar_url)
            await ctx.send (embed = emb)
            print(f'[Logs:info] Информация о категориях команд бота была выведена для пользователя {user} | {prefix}хелп [RU]')
        if title != None:
            if title == 'Инфо' or title == 'инфо' or title == 'Информация' or title == 'информация':
                emb = discord.Embed(title = f'Доступные команды группы: `Информация`', description = f'**Префикс: `{prefix}`**', color = cogs_color['HELP NONE COLOR'])
                emb.add_field(name = f'{prefix}хелп', value = f'Справка по всем команда и их категориям', inline=False)
                emb.add_field(name = f'{prefix}none', value = f'none', inline=False)
                emb.add_field(name = f'{prefix}none', value = f'none', inline=False)
                emb.add_field(name = f'{prefix}none', value = f'none', inline=False)
                emb.add_field(name = f'{prefix}none', value = f'none', inline=False)
                emb.add_field(name = f'Внимание! Если заметили ошибки или недочёты, пожалуйста, опишите её в команде {prefix}bugs [NO WORK], будем благодарны!', value = f'Всего команд: {com_value}', inline=False)
                emb.set_thumbnail(url = self.client.user.avatar_url)
                emb.set_footer(text = f'{copyright_ru}', icon_url = self.client.user.avatar_url)
                await ctx.send (embed = emb)    
                print(f'[Logs:info] Информация о категории "Информация" была выведена для пользователя {user} | {prefix}хелп инфо [RU]')   
            if title == 'Модерирование' or title == 'модерирование' or title == 'Модер' or title == 'модер' or title == 'Модерация' or title == 'модерация':
                emb = discord.Embed(title = f'Доступные команды группы: `Модерация`', description = f'**Префикс: `{prefix}`**', color = cogs_color['HELP NONE COLOR'])
                emb.add_field(name = f'{prefix}none', value = f'none', inline=False)
                emb.add_field(name = f'{prefix}none', value = f'none', inline=False)
                emb.add_field(name = f'{prefix}none', value = f'none', inline=False)
                emb.add_field(name = f'{prefix}none', value = f'none', inline=False)
                emb.add_field(name = f'{prefix}none', value = f'none', inline=False)
                emb.add_field(name = f'Внимание! Если заметили ошибки или недочёты, пожалуйста, опишите её в команде {prefix}bugs [NO WORK], будем благодарны!', value = f'Всего команд: {com_value}', inline=False)
                emb.set_thumbnail(url = self.client.user.avatar_url)
                emb.set_footer(text = f'{copyright_ru}', icon_url = self.client.user.avatar_url)
                await ctx.send (embed = emb)    
                print(f'[Logs:info] Информация о категории "Модерация" была выведена для пользователя {user} | {prefix}хелп модер [RU]')
            if title == 'Действия' or title == 'действия':
                emb = discord.Embed(title = f'Доступные команды группы: `Действия`', description = f'**Префикс: `{prefix}`**', color = cogs_color['HELP NONE COLOR'])
                emb.add_field(name = f'{prefix}none', value = f'none', inline=False)
                emb.add_field(name = f'{prefix}none', value = f'none', inline=False)
                emb.add_field(name = f'{prefix}none', value = f'none', inline=False)
                emb.add_field(name = f'{prefix}none', value = f'none', inline=False)
                emb.add_field(name = f'{prefix}none', value = f'none', inline=False)
                emb.add_field(name = f'Внимание! Если заметили ошибки или недочёты, пожалуйста, опишите её в команде {prefix}bugs [NO WORK], будем благодарны!', value = f'Всего команд: {com_value}', inline=False)
                emb.set_thumbnail(url = self.client.user.avatar_url)
                emb.set_footer(text = f'{copyright_ru}', icon_url = self.client.user.avatar_url)
                await ctx.send (embed = emb)    
                print(f'[Logs:info] Информация о категории "Действия" была выведена для пользователя {user} | {prefix}хелп действия [RU]')                                      
            if title == 'Весёлое' or title == 'весёлое':
                emb = discord.Embed(title = f'Доступные команды группы: `Весёлое`', description = f'**Префикс: `{prefix}`**', color = cogs_color['HELP NONE COLOR'])
                emb.add_field(name = f'{prefix}none', value = f'none', inline=False)
                emb.add_field(name = f'{prefix}none', value = f'none', inline=False)
                emb.add_field(name = f'{prefix}none', value = f'none', inline=False)
                emb.add_field(name = f'{prefix}none', value = f'none', inline=False)
                emb.add_field(name = f'{prefix}none', value = f'none', inline=False)
                emb.add_field(name = f'Внимание! Если заметили ошибки или недочёты, пожалуйста, опишите её в команде {prefix}bugs [NO WORK], будем благодарны!', value = f'Всего команд: {com_value}', inline=False)
                emb.set_thumbnail(url = self.client.user.avatar_url)
                emb.set_footer(text = f'{copyright_ru}', icon_url = self.client.user.avatar_url)
                await ctx.send (embed = emb)    
                print(f'[Logs:info] Информация о категории "Весёлое" была выведена для пользователя {user} | {prefix}хелп весёлое [RU]')   
            if title == 'Утилиты' or title == 'утилиты' or title == 'Утил' or title == 'утил':
                emb = discord.Embed(title = f'Доступные команды группы: `Утилиты`', description = f'**Префикс: `{prefix}`**', color = cogs_color['HELP NONE COLOR'])
                emb.add_field(name = f'{prefix}аватар', value = f'Показать аватар участника', inline=False)
                emb.add_field(name = f'{prefix}ранд', value = f'Получить рандомное число', inline=False)
                emb.add_field(name = f'{prefix}тайм', value = f'Показывает текущее время по МСК', inline=False)
                emb.add_field(name = f'{prefix}вики', value = f'Выводит искомую информацию с википедии', inline=False)
                emb.add_field(name = f'{prefix}none', value = f'none', inline=False)
                emb.add_field(name = f'Внимание! Если заметили ошибки или недочёты, пожалуйста, опишите её в команде {prefix}bugs [NO WORK], будем благодарны!', value = f'Всего команд: {com_value}', inline=False)
                emb.set_thumbnail(url = self.client.user.avatar_url)
                emb.set_footer(text = f'{copyright_ru}', icon_url = self.client.user.avatar_url)
                await ctx.send (embed = emb)    
                print(f'[Logs:info] Информация о категории "Утилиты" была выведена для пользователя {user} | {prefix}хелп утилиты [RU]')                  
            
def setup(client):
    client.add_cog(info(client))