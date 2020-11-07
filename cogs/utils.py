import discord
from discord.ext import commands
import os, random, datetime, clock, config, wikipedia, pytz
from config import cogs_color, settings, quick_messages, other_settings
prefix = settings['PREFIX']
unknown_log = quick_messages['UNKNOWN ERROR LOG']
unknown = quick_messages['UNKNOWN ERROR']
copyright_ru = quick_messages['COPYRIGHT RU']
copyright_en = quick_messages['COPYRIGHT EN']
class utils(commands.Cog):
    
    def __init__(self, client):
        self.client = client
    
#   ███████╗███╗░░██╗░██████╗░██╗░░░░░██╗░██████╗██╗░░██╗
#   ██╔════╝████╗░██║██╔════╝░██║░░░░░██║██╔════╝██║░░██║
#   █████╗░░██╔██╗██║██║░░██╗░██║░░░░░██║╚█████╗░███████║
#   ██╔══╝░░██║╚████║██║░░╚██╗██║░░░░░██║░╚═══██╗██╔══██║
#   ███████╗██║░╚███║╚██████╔╝███████╗██║██████╔╝██║░░██║
#   ╚══════╝╚═╝░░╚══╝░╚═════╝░╚══════╝╚═╝╚═════╝░╚═╝░░╚═╝ 
    @commands.command(aliases = ['Avatarka', 'avatarka', 'Ava', 'ava', 'Avatar', 'avatar'])    
    async def __avatar(self, ctx, member: discord.Member = None):
        user = ctx.message.author if (member == None) else member
        emb = discord.Embed(title = f'User avatar {user}', color = cogs_color['AVATAR COLOR'])
        emb.set_image(url = user.avatar_url)
        await ctx.send(embed = emb)
        print(f'[Logs:utils] Аватар пользователя {user} был выведен | {prefix}avatar [EU]')
        
    @commands.command(aliases = ['Random', 'random', 'Rand', 'rand'])    
    async def __random(self, ctx, count = None):
        if count == None:
            emb = discord.Embed(description = f'Example: `{prefix}random 5` - Will print a number from 1 to 5.', color = cogs_color['RANDOM COLOR'])
            emb.set_footer(text = f'{copyright_en}', icon_url = self.client.user.avatar_url)
            await ctx.send(embed = emb)
            print(f'[Logs:utils] Максимальное число не было указано | {prefix}random [EU]')
        else:
            try:
                await ctx.send(str(random.randint(int(1), int(count))))
                print(f'[Logs:utils] Рандомное число было успешно сгенерировано | {prefix}random [EU]')
            except ValueError:
                emb = discord.Embed(description = 'Mistake! Third party symbols were found!', color = cogs_color['RANDOM COLOR ERROR'])
                emb.set_footer(text = f'{copyright_en}', icon_url = self.client.user.avatar_url)
                await ctx.send(embed = emb)
                print(f'[Logs:error] Ошибка! Были найдены сторонние символы! | {prefix}random [EU]')    
                
    @commands.command(aliases = ['Time', 'time', 'Clock', 'clock'])
    async def __time(self, ctx):
        tz_paris = pytz.timezone('Europe/Paris')
        clock_dt = datetime.datetime.now(tz_paris)
        time_clock = (f"{clock_dt.hour}{clock_dt.minute}")

        time_clock = float(datetime.datetime.strptime(time_clock, '%H%M').strftime('%I.%M').lower())
        print(f'[Logs:utils] Время было успешно выведено | {prefix}time [EU]')

        table_clock = clock.diff
        result_clock = table_clock.get(time_clock, table_clock[min(table_clock.keys(), key = lambda k: abs(k-time_clock))])


        emb = discord.Embed( title = 'Online time', description = 'Current time by CET', colour = cogs_color['TIME COLOR'], url = 'https://time.is/CET' )

        emb.set_footer(text = f'{copyright_en}', icon_url = self.client.user.avatar_url)
        emb.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
        emb.set_thumbnail(url = str(result_clock))

        dt = datetime.datetime.now(tz_paris)
        data = (f'{ dt.day }.{ dt.month }.{ dt.year }')
        time = (f'{ dt.hour }:{ dt.minute }')

        emb.add_field(name = f'Date: {data}', value = f'Time: {time}')

        await ctx.send(embed = emb)
        
    @commands.command(aliases = ['Wiki', 'wiki', 'Wikipedia', 'wikipedia'])
    async def __wiki(self, ctx, *, text = None):
        if text == None:
            emb = discord.Embed(description = f'Example: `{prefix}wiki discord` - Find information about discord on wikipedia.')
            emb.set_footer(text = f'{copyright_en}', icon_url = self.client.user.avatar_url)
            await ctx.send(embed = emb)
            print(f'[Logs:error] Искомая информация не была введена | {prefix}wiki [EU]')
        else:
            try:
                wikipedia.set_lang('eu')
                new_page = wikipedia.page(text)
                summ = wikipedia.summary(text)
                emb = discord.Embed(title = new_page.title, description = summ, color = cogs_color['WIKIPEDIA COLOR'])
                emb.set_author(name = 'More information here! Click!', url = new_page.url, icon_url = 'https://upload.wikimedia.org/wikipedia/commons/thumb/8/80/Wikipedia-logo-v2.svg/1200px-Wikipedia-logo-v2.svg.png')
                emb.set_footer(icon_url = self.client.user.avatar_url, text = f'{copyright_en}')
                await ctx.send(embed = emb)
                print(f'[Logs:utils] Информация о "{text}" была выведена | {prefix}wiki [EU]')    
            except:
                emb = discord.Embed(description = f'An unknown error has occurred!', color = cogs_color['WIKIPEDIA COLOR ERROR'])   
                emb.set_footer(text = f'{copyright_en}', icon_url = self.client.user.avatar_url)
                await ctx.send(embed = emb)
                print(f'{unknown_log} {prefix}wiki [EU]')
       
                
#██████╗░██╗░░░██╗░██████╗░██████╗██╗░█████╗░███╗░░██╗
#██╔══██╗██║░░░██║██╔════╝██╔════╝██║██╔══██╗████╗░██║
#██████╔╝██║░░░██║╚█████╗░╚█████╗░██║███████║██╔██╗██║
#██╔══██╗██║░░░██║░╚═══██╗░╚═══██╗██║██╔══██║██║╚████║
#██║░░██║╚██████╔╝██████╔╝██████╔╝██║██║░░██║██║░╚███║
#╚═╝░░╚═╝░╚═════╝░╚═════╝░╚═════╝░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝               
    @commands.command(aliases = ['Аватарка', 'аватарка', 'Ава', 'ава', 'Аватар', 'аватар'])    
    async def ___avatar(self, ctx, member: discord.Member = None):
        user = ctx.message.author if (member == None) else member
        emb = discord.Embed(title = f'Аватар пользователя {user}', color = cogs_color['AVATAR COLOR'])
        emb.set_image(url = user.avatar_url)
        await ctx.send(embed = emb)
        print(f'[Logs:utils] Аватар пользователя {user} был выведен | {prefix}аватар [RU]')
        
    @commands.command(aliases = ['Рандом', 'рандом', 'Ранд', 'ранд'])    
    async def ___random(self, ctx, count = None):
        if count == None:
            emb = discord.Embed(description = f'Пример: `{prefix}рандом 5` - Будет выведено число от 1 до 5.', color = cogs_color['RANDOM COLOR'])
            emb.set_footer(text = f'{copyright_ru}', icon_url = self.client.user.avatar_url)
            await ctx.send(embed = emb)
            print(f'[Logs:utils] Максимальное число не было указано | {prefix}random [RU]')
        else:
            try:
                await ctx.send(str(random.randint(int(1), int(count))))
                print(f'[Logs:utils] Рандомное число было успешно сгенерировано | {prefix}random [RU]')
            except ValueError:
                msg = await ctx.send(embed = discord.Embed(description='Ошибка! Были найдены сторонние символы!', color = cogs_color['RANDOM COLOR ERROR']))
                emb.set_footer(text = f'{copyright_ru}', icon_url = self.client.user.avatar_url)
                print(f'[Logs:error] Ошибка! Были найдены сторонние символы! | {prefix}random [RU]')                          
    
    @commands.command(aliases = ['Время', 'время', 'Часы', 'часы', 'Тайм', 'тайм'])
    async def ___time(self, ctx):
        clock_dt = datetime.datetime.now()
        time_clock = (f"{clock_dt.hour}{clock_dt.minute}")

        time_clock = float(datetime.datetime.strptime(time_clock, '%H%M').strftime('%I.%M').lower())
        print(f'[Logs:utils] Вывожу время | {prefix}time [RU]')

        table_clock = clock.diff
        result_clock = table_clock.get(time_clock, table_clock[min(table_clock.keys(), key=lambda k: abs(k-time_clock))])


        emb = discord.Embed(title = 'Время онлайн', description = 'Текущее время по МСК', colour = cogs_color['TIME COLOR'], url = 'https://time100.ru/')

        emb.set_footer(text = f'{copyright_ru}', icon_url = self.client.user.avatar_url)
        emb.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
        emb.set_thumbnail(url = str(result_clock))

        dt = datetime.datetime.now()
        data = (f'{dt.day}.{dt.month}.{dt.year}')
        time = (f'{dt.hour}:{dt.minute}')

        emb.add_field(name = f'Дата: {data}', value = f'Время: {time}')

        await ctx.send(embed = emb)    
        
    @commands.command(aliases = ['Вики', 'вики', 'Википедия', 'википедия'])
    async def ___wiki(self, ctx, *, text = None):
        if text == None:
            emb = discord.Embed(description = f'Пример: `{prefix}вики discord` - Будет выведена информация о дискорде.')
            emb.set_footer(text = f'{copyright_ru}', icon_url = self.client.user.avatar_url)
            await ctx.send(embed = emb)
            print(f'[Logs:error] Искомая информация не была введена | {prefix}wiki [RU]')
        else:
            try:
                wikipedia.set_lang('ru')
                new_page = wikipedia.page(text)
                summ = wikipedia.summary(text)
                emb = discord.Embed(title = new_page.title, description = summ, color = cogs_color['WIKIPEDIA COLOR'])
                emb.set_author(name = 'Больше информации здесь! Кликай!', url = new_page.url, icon_url = 'https://upload.wikimedia.org/wikipedia/commons/thumb/8/80/Wikipedia-logo-v2.svg/1200px-Wikipedia-logo-v2.svg.png')
                emb.set_footer(icon_url = self.client.user.avatar_url, text = f"{copyright_ru}")
                await ctx.send(embed = emb)
                print(f'[Logs:utils] Информация о "{text}" была выведена | {prefix}wiki [RU]')
            except:
                emb = discord.Embed(description = f'{unknown}', color = cogs_color['WIKIPEDIA COLOR ERROR'])   
                emb.set_footer(text = f'{copyright_ru}', icon_url = self.client.user.avatar_url)
                await ctx.send(embed = emb)
                print(f'{unknown_log} {prefix}wiki [EU]')            
                  
def setup(client):
    client.add_cog(utils(client))
