import discord
from discord.ext import commands
import random, datetime, config, wikipedia, pytz, useful
from useful import diff, translit_abc, ru_layout
from config import cogs_color, settings, quick_messages, other_settings, fast_link
prefix = settings['PREFIX']
unknown_log = quick_messages['UNKNOWN ERROR LOG']
unknown = quick_messages['UNKNOWN ERROR']
unknown_en = quick_messages['UNKNOWN ERROR EN']
copyright_ru = quick_messages['COPYRIGHT RU']
copyright_en = quick_messages['COPYRIGHT EN']
third_sym_log = quick_messages['THIRD PARTY SYM ERROR LOG']
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
        
    # @commands.command(aliases = ['Random', 'random', 'Rand', 'rand'])    
    # async def __random(self, ctx, count = None):
    #     if count == None:
    #         emb = discord.Embed(description = f'Example: `{prefix}random 5` - Will print a number from 1 to 5.', color = cogs_color['RANDOM COLOR'])
    #         emb.set_footer(text = copyright_en, icon_url = self.client.user.avatar_url)
    #         await ctx.send(embed = emb)
    #         print(f'[Logs:utils] Максимальное число не было указано | {prefix}random [EU]')
    #     else:
    #         try:
    #             await ctx.send(str(random.randint(int(1), int(count))))
    #             print(f'[Logs:utils] Рандомное число было успешно сгенерировано | {prefix}random [EU]')
    #         except ValueError:
    #             emb = discord.Embed(description = quick_messages['THIRD PARTY SYM ERROR EN'], color = cogs_color['RANDOM COLOR ERROR'])
    #             emb.set_footer(text = copyright_en, icon_url = self.client.user.avatar_url)
    #             await ctx.send(embed = emb)
    #             print(f'{third_sym_log} {prefix}random [EU]')    
    
    @commands.command(aliases = ['Random', 'random', 'Rand', 'rand'])  
    async def __random(self, ctx, count = None, count1 = None):
        if count == None and count1 == None:
            emb = discord.Embed(description = f'Example: `{prefix}random 5` - Will print a number from 1 to 5.\n Example: `{prefix}random 5 10` - Will print a number from 5 to 10.', color = cogs_color['RANDOM COLOR'])
            emb.set_footer(text = copyright_en, icon_url = self.client.user.avatar_url)
            await ctx.send(embed = emb)
            print(f'[Logs:utils] Максимальное число не было указано | {prefix}rtc [EU]')
        if count != None and count1 == None:
            try:
                await ctx.send(str(random.randint(int(1), int(count))))
                print(f'[Logs:utils] Рандомное число было успешно сгенерировано | {prefix}rtc [EU]')
            except ValueError:
                emb = discord.Embed(description = quick_messages['THIRD PARTY SYM ERROR EN'], color = cogs_color['RANDOM COLOR ERROR'])
                emb.set_footer(text = copyright_en, icon_url = self.client.user.avatar_url)
                await ctx.send(embed = emb)
                print(f'{third_sym_log} {prefix}rtc [EU]')   
        if count != None and count1 != None:
            try:
                await ctx.send(str(random.randint(int(count), int(count1))))
                print(f'[Logs:utils] Рандомное число было успешно сгенерировано | {prefix}rtc [EU]')
            except ValueError:
                emb = discord.Embed(description = quick_messages['THIRD PARTY SYM ERROR EN'], color = cogs_color['RANDOM COLOR ERROR'])
                emb.set_footer(text = copyright_en, icon_url = self.client.user.avatar_url)
                await ctx.send(embed = emb)
                print(f'{third_sym_log} {prefix}rtc [EU]') 
                            
    @commands.command(aliases = ['Time', 'time', 'Clock', 'clock'])
    async def __time(self, ctx):
        tz_paris = pytz.timezone('Europe/Paris')
        clock_dt = datetime.datetime.now(tz_paris)
        time_clock = (f"{clock_dt.hour}{clock_dt.minute}")

        time_clock = float(datetime.datetime.strptime(time_clock, '%H%M').strftime('%I.%M').lower())
        print(f'[Logs:utils] Часы были успешно выведено | {prefix}time [EU]')

        table_clock = useful.diff # or table_clock = diff (no difference)
        result_clock = table_clock.get(time_clock, table_clock[min(table_clock.keys(), key = lambda k: abs(k-time_clock))])


        emb = discord.Embed( title = 'Online time', description = 'Current time by CET', colour = cogs_color['TIME COLOR'], url = fast_link['TIME CET'])

        emb.set_footer(text = copyright_en, icon_url = self.client.user.avatar_url)
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
            emb.set_footer(text = copyright_en, icon_url = self.client.user.avatar_url)
            await ctx.send(embed = emb)
            print(f'[Logs:error] Искомая информация не была введена | {prefix}wiki [EU]')
        else:
            try:
                wikipedia.set_lang('eu')
                new_page = wikipedia.page(text)
                summ = wikipedia.summary(text)
                emb = discord.Embed(title = new_page.title, description = summ, color = cogs_color['WIKIPEDIA COLOR'])
                emb.set_author(name = 'More information here! Click!', url = new_page.url, icon_url = fast_link['WIKIPEDIA IMG'])
                emb.set_footer(icon_url = self.client.user.avatar_url, text = copyright_en)
                await ctx.send(embed = emb)
                print(f'[Logs:utils] Информация о "{text}" была выведена | {prefix}wiki [EU]')    
            except:
                emb = discord.Embed(description = unknown_en, color = cogs_color['WIKIPEDIA COLOR ERROR'])   
                emb.set_footer(text = copyright_en, icon_url = self.client.user.avatar_url)
                await ctx.send(embed = emb)
                print(f'{unknown_log} {prefix}wiki [EU]')
       
    @commands.command(aliases = ['Achievement', 'achievement', 'Mine_achievement', 'mine_achievement'])
    async def __minecraft_achievement(self, ctx, *, name:str = None):
        a = random.randint(1, 40)
        name2 = name.replace(' ', '+')
        url = f'{fast_link["MCACH"]}{a}/Achievement+Get%21/{name2}'
        emb = discord.Embed(description = f'[Achievement!]({url})', color = cogs_color["MCACH COLOR"])
        emb.set_footer(text = copyright_en, icon_url = self.client.user.avatar_url)
        emb.set_image(url = url)
        await ctx.send(embed=emb)
        print(f'[Logs:utils] Майнкрафт достижение было успешно создано | {prefix}achievement [EN]')          
        
        
    @commands.command(aliases = ['Reverse', 'reverse'])
    async def __reverse(self, ctx, *, text: str):
        t_rev = text[::-1].replace("@", "@\u200B").replace("&", "&\u200B")
        emb = discord.Embed(title = 'Reverse text:', description = t_rev, color = cogs_color["REVERSE COLOR"])
        emb.set_footer(text = copyright_en, icon_url = self.client.user.avatar_url)
        await ctx.send(embed=emb)
        print(f"[Logs:utils] Команда была успешно использована | {prefix}reverse [EU]")    
        
    @commands.command(aliases = ['Forgot_layout', 'forgot_layout', 'Forgotlayout', 'forgotlayout', 'Ru_layout', 'ru_layout', 'Rulayout', 'rulayout'])
    async def __Forgot_layout(self, ctx, *, message = None):
        if message == None:
            emb = discord.Embed(description = f'Example: `{prefix}ru_layout ghbdtn` - A message will be displayed привет.', color = cogs_color['LAYOUT COLOR EXAMPLE'])
            emb.set_footer(text = copyright_en, icon_url = self.client.user.avatar_url)
            await ctx.send(embed = emb)
            print(f'[Logs:error] Один из аргументов не был введен корректно | {prefix}ru_layout [EU]')
        else:
            itog = ""
            errors = ""
            for i in message:
                if i.lower() in ru_layout:
                    itog += ru_layout[i.lower()]
                else:
                    errors += f"`{i}` "
            if len(errors) <= 0:
                 errors_itog = ""
            else:
                errors_itog = f"\nНепереведенные символы: {errors}"
                print(f"[Logs:utils] [Warning] Перевод содержит непереведенные символы | {prefix}ru_layout [EU]")

            if len(itog) <= 0:
                emb = discord.Embed(description = 'Failed to translate message! :pencil:\nPerhaps you are trying to translate transliteration into a Russian word', color = cogs_color['LAYOUT COLOR ERROR'])
                emb.set_footer(text = copyright_en, icon_url = self.client.user.avatar_url)
                await ctx.send(embed = emb)
                print(f"[Logs:utils] [Error] Не удалось перевести сообщение | {prefix}ru_layout [EU]")
            else:
                itog_new = f"Translation: {itog}"   
                emb = discord.Embed(description = f'{itog_new}{errors_itog}', color = cogs_color['LAYOUT COLOR EXAMPLE'])
                emb.set_footer(text = copyright_en, icon_url = self.client.user.avatar_url)
                await ctx.send(embed = emb)
                print(f"[Logs:utils] Текст был успешно переведен на русскую раскладку | {prefix}ru_layout [EU]")
                  
    @commands.command(aliases = ['Translit', 'translit'])
    async def __translit(self, ctx, *, message = None):  
        if message == None:
            emb = discord.Embed(description = f'Example: `{prefix}translit privet` - A message will be displayed привет.', color = cogs_color['TRANSLIT COLOR EXAMPLE'])
            emb.set_footer(text = copyright_en, icon_url = self.client.user.avatar_url)
            await ctx.send(embed = emb)
            print(f'[Logs:error] Один из аргументов не был введен корректно | {prefix}транслит [RU]')
        else:
            itog = ""
            errors = ""
            for i in message:
                if i.lower() in translit_abc:
                    itog += translit_abc[i.lower()]
                else:
                    errors += f"`{i}` "
            if len(errors) <= 0:
                 errors_itog = ""
            else:
                errors_itog = f"\nUntranslated characters: {errors}"
                print(f"[Logs:utils] [Warning] Перевод содержит непереведенные символы | {prefix}транслит [RU]")

            if len(itog) <= 0:
                emb = discord.Embed(description = 'Failed to translate message! :pencil:\nPerhaps you are trying to translate a Russian word into transliteration', color = cogs_color['TRANSLIT COLOR ERROR'])
                emb.set_footer(text = copyright_en, icon_url = self.client.user.avatar_url)
                await ctx.send(embed = emb)
                print(f"[Logs:utils] [Error] Не удалось перевести сообщение | {prefix}транслит [RU]")
            else:
                itog_new = f"Translation: {itog}"
                emb = discord.Embed(description = f'{itog_new}{errors_itog}', color = cogs_color['LAYOUT COLOR EXAMPLE'])
                emb.set_footer(text = copyright_en, icon_url = self.client.user.avatar_url)
                await ctx.send(embed = emb) 
                print(f"[Logs:utils] Текст был успешно переведен на русскую раскладку | {prefix}транслит [RU]")      
                
                     
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
        
    # @commands.command(aliases = ['Рандом', 'рандом', 'Ранд', 'ранд'])    
    # async def ___random(self, ctx, count = None):
    #     if count == None:
    #         emb = discord.Embed(description = f'Пример: `{prefix}рандом 5` - Будет выведено число от 1 до 5.', color = cogs_color['RANDOM COLOR'])
    #         emb.set_footer(text = copyright_ru, icon_url = self.client.user.avatar_url)
    #         await ctx.send(embed = emb)
    #         print(f'[Logs:utils] Максимальное число не было указано | {prefix}random [RU]')
    #     else:
    #         try:
    #             await ctx.send(str(random.randint(int(1), int(count))))
    #             print(f'[Logs:utils] Рандомное число было успешно сгенерировано | {prefix}random [RU]')
    #         except ValueError:
    #             emb = discord.Embed(description = quick_messages['THIRD PARTY SYM ERROR'], color = cogs_color['RANDOM COLOR ERROR'])
    #             emb.set_footer(text = copyright_ru, icon_url = self.client.user.avatar_url)
    #             await ctx.send(embed = emb)
    #             print(f'{third_sym_log} {prefix}random [RU]')                          
    
    @commands.command(aliases = ['Рандом', 'рандом', 'Ранд', 'ранд'])  
    async def ___random(self, ctx, count = None, count1 = None):
        if count == None and count1 == None:
            emb = discord.Embed(description = f'Пример: `{prefix}рандом 5` - Будет выведено число от 1 до 5.\n Пример 2: `{prefix}рандом 5 10` - Будет выведено число от 5 до 10.', color = cogs_color['RANDOM COLOR'])
            emb.set_footer(text = copyright_ru, icon_url = self.client.user.avatar_url)
            await ctx.send(embed = emb)
            print(f'[Logs:utils] Максимальное число не было указано | {prefix}rtc [RU]')
        if count != None and count1 == None:
            try:
                await ctx.send(str(random.randint(int(1), int(count))))
                print(f'[Logs:utils] Рандомное число было успешно сгенерировано | {prefix}rtc [RU]')
            except ValueError:
                emb = discord.Embed(description = quick_messages['THIRD PARTY SYM ERROR'], color = cogs_color['RANDOM COLOR ERROR'])
                emb.set_footer(text = copyright_ru, icon_url = self.client.user.avatar_url)
                await ctx.send(embed = emb)
                print(f'{third_sym_log} {prefix}rtc [RU]')   
        if count != None and count1 != None:
            try:
                await ctx.send(str(random.randint(int(count), int(count1))))
                print(f'[Logs:utils] Рандомное число было успешно сгенерировано | {prefix}rtc [RU]')
            except ValueError:
                emb = discord.Embed(description = quick_messages['THIRD PARTY SYM ERROR'], color = cogs_color['RANDOM COLOR ERROR'])
                emb.set_footer(text = copyright_ru, icon_url = self.client.user.avatar_url)
                await ctx.send(embed = emb)
                print(f'{third_sym_log} {prefix}rtc [RU]') 
                
    @commands.command(aliases = ['Время', 'время', 'Часы', 'часы', 'Тайм', 'тайм'])
    async def ___time(self, ctx):
        clock_dt = datetime.datetime.now()
        time_clock = (f"{clock_dt.hour}{clock_dt.minute}")

        time_clock = float(datetime.datetime.strptime(time_clock, '%H%M').strftime('%I.%M').lower())
        print(f'[Logs:utils] Часы были успешно выведены | {prefix}time [RU]')

        table_clock = useful.diff # or table_clock = diff (no difference)
        result_clock = table_clock.get(time_clock, table_clock[min(table_clock.keys(), key=lambda k: abs(k-time_clock))])


        emb = discord.Embed(title = 'Время онлайн', description = 'Текущее время по МСК', colour = cogs_color['TIME COLOR'], url = fast_link['TIME MSC'])

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
            emb.set_footer(text = copyright_ru, icon_url = self.client.user.avatar_url)
            await ctx.send(embed = emb)
            print(f'[Logs:error] Искомая информация не была введена | {prefix}wiki [RU]')
        else:
            try:
                wikipedia.set_lang('ru')
                new_page = wikipedia.page(text)
                summ = wikipedia.summary(text)
                emb = discord.Embed(title = new_page.title, description = summ, color = cogs_color['WIKIPEDIA COLOR'])
                emb.set_author(name = 'Больше информации здесь! Кликай!', url = new_page.url, icon_url = fast_link['WIKIPEDIA IMG'])
                emb.set_footer(icon_url = self.client.user.avatar_url, text = copyright_ru)
                await ctx.send(embed = emb)
                print(f'[Logs:utils] Информация о "{text}" была выведена | {prefix}wiki [RU]')
            except:
                emb = discord.Embed(description = unknown, color = cogs_color['WIKIPEDIA COLOR ERROR'])   
                emb.set_footer(text = copyright_ru, icon_url = self.client.user.avatar_url)
                await ctx.send(embed = emb)
                print(f'{unknown_log} {prefix}wiki [RU]')            
    
    @commands.command(aliases = ['Ачивка', 'ачивка', 'Достижение', 'достижение', 'Майн_ачивка', 'майн_ачивка'])
    async def ___minecraft_achievement(self, ctx, *, name:str = None):
        a = random.randint(1, 40)
        name2 = name.replace(' ', '+')
        url = f'{fast_link["MCACH"]}{a}/Achievement+Get%21/{name2}'
        emb = discord.Embed(description = f'[Достижение!]({url})', color = cogs_color["MCACH COLOR"])
        emb.set_footer(text = copyright_ru, icon_url = self.client.user.avatar_url)
        emb.set_image(url = url)
        await ctx.send(embed=emb)
        print(f'[Logs:utils] Майнкрафт достижение было успешно создано | {prefix}достижение [RU]')   
        
    @commands.command(aliases = ['Реверс', 'реверс', 'Обратный', 'обратный'])
    async def ___reverse(self, ctx, *, text: str):
        t_rev = text[::-1].replace("@", "@\u200B").replace("&", "&\u200B")
        emb = discord.Embed(title = 'Обратный текст:', description = t_rev, color = cogs_color["REVERSE COLOR"])
        emb.set_footer(text = copyright_ru, icon_url = self.client.user.avatar_url)
        await ctx.send(embed=emb)
        print(f"[Logs:utils] Текст был успешно отражен в обратную сторону | {prefix}реверс [RU]")   
    
    @commands.command(aliases = ['Забыл_раскладку', 'забыл_раскладку', 'Забылраскладку', 'забылраскладку', 'Ру_раскладка', 'ру_раскладка', 'Рураскладка', 'рураскладка'])
    async def ___Forgot_layout(self, ctx, *, message = None):
        if message == None:
            emb = discord.Embed(description = f'Пример: `{prefix}ру_раскладка ghbdtn` - Будет выведено сообщение привет.', color = cogs_color['LAYOUT COLOR EXAMPLE'])
            emb.set_footer(text = copyright_ru, icon_url = self.client.user.avatar_url)
            await ctx.send(embed = emb)
            print(f'[Logs:error] Один из аргументов не был введен корректно | {prefix}ру_раскладка [RU]')
        else:
            itog = ""
            errors = ""
            for i in message:
                if i.lower() in ru_layout:
                    itog += ru_layout[i.lower()]
                else:
                    errors += f"`{i}` "
            if len(errors) <= 0:
                 errors_itog = ""
            else:
                errors_itog = f"\nНепереведенные символы: {errors}"
                print(f"[Logs:utils] [Warning] Перевод содержит непереведенные символы | {prefix}ру_раскладка [RU]")

            if len(itog) <= 0:
                emb = discord.Embed(description = 'Не удалось перевести сообщение! :pencil:\nВозможно, вы пытаетесь перевести транслит в русское слово', color = cogs_color['LAYOUT COLOR ERROR'])
                emb.set_footer(text = copyright_ru, icon_url = self.client.user.avatar_url)
                await ctx.send(embed = emb)
                print(f"[Logs:utils] [Error] Не удалось перевести сообщение | {prefix}ру_раскладка [RU]")
            else:
                itog_new = f"Перевод: {itog}"   
                emb = discord.Embed(description = f'{itog_new}{errors_itog}', color = cogs_color['LAYOUT COLOR EXAMPLE'])
                emb.set_footer(text = copyright_ru, icon_url = self.client.user.avatar_url)
                await ctx.send(embed = emb)
                print(f"[Logs:utils] Текст был успешно переведен на русскую раскладку | {prefix}ру_раскладка [RU]")
                  
    @commands.command(aliases = ['Транслит', 'транслит'])
    async def ___translit(self, ctx, *, message = None):  
        if message == None:
            emb = discord.Embed(description = f'Пример: `{prefix}транслит privet` - Будет выведено сообщение привет.', color = cogs_color['TRANSLIT COLOR EXAMPLE'])
            emb.set_footer(text = copyright_ru, icon_url = self.client.user.avatar_url)
            await ctx.send(embed = emb)
            print(f'[Logs:error] Один из аргументов не был введен корректно | {prefix}транслит [RU]')
        else:
            itog = ""
            errors = ""
            for i in message:
                if i.lower() in translit_abc:
                    itog += translit_abc[i.lower()]
                else:
                    errors += f"`{i}` "
            if len(errors) <= 0:
                 errors_itog = ""
            else:
                errors_itog = f"\nНепереведенные символы: {errors}"
                print(f"[Logs:utils] [Warning] Перевод содержит непереведенные символы | {prefix}транслит [RU]")

            if len(itog) <= 0:
                #itog_new = "Перевода нет!"
                emb = discord.Embed(description = 'Не удалось перевести сообщение! :pencil:\nВозможно, вы пытаетесь перевести русское слово в транслит', color = cogs_color['TRANSLIT COLOR ERROR'])
                emb.set_footer(text = copyright_ru, icon_url = self.client.user.avatar_url)
                await ctx.send(embed = emb)
                print(f"[Logs:utils] [Error] Не удалось перевести сообщение | {prefix}транслит [RU]")
            else:
                itog_new = f"Перевод: {itog}"
                emb = discord.Embed(description = f'{itog_new}{errors_itog}', color = cogs_color['LAYOUT COLOR EXAMPLE'])
                emb.set_footer(text = copyright_ru, icon_url = self.client.user.avatar_url)
                await ctx.send(embed = emb) 
                print(f"[Logs:utils] Текст был успешно переведен на русскую раскладку | {prefix}транслит [RU]")   
                
                         
def setup(client):
    client.add_cog(utils(client))
