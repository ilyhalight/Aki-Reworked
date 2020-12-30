import discord
from discord.ext import commands
from useful import links, defcl, other, prefix, copyright_ru
com_value = other['commands']
class Help(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases = ['Help', 'help', 'Хелп', 'хелп'])
    async def __help(self, ctx, *, title = None):
        user = ctx.message.author
        if title == None:
            emb = discord.Embed(title = f'Доступные команды:', description = f'**Префикс: `{prefix}`**', color = defcl['help'])
            emb.add_field(name = f'Информация ({prefix}хелп Информация)', value = '`В данном разделе содержатся все информационные команды`', inline = False)
            emb.add_field(name = f'Модерация ({prefix}ахелп)', value = '`В этом разделе собраны все команды администратора`', inline = False)
            emb.add_field(name = f'Действия ({prefix}хелп Действия)', value = '`В данном разделе содержатся все РП команды`', inline = False)
            emb.add_field(name = f'Весёлое ({prefix}хелп Весёлое)', value = '`В данном разделе содержатся все весёлые команды`', inline = False)
            emb.add_field(name = f'Утилиты ({prefix}хелп Утилиты)', value = '`В данном разделе содержатся все утилиты`', inline = False)
            emb.add_field(name = f'Внимание! Если заметили ошибки или недочёты, пожалуйста, опишите их на нашем сервере {links["discord server"]}, будем благодарны!', value = f'Всего команд: {com_value}', inline = False)
            emb.set_thumbnail(url = self.bot.user.avatar_url)
            emb.set_footer(text = copyright_ru, icon_url = self.bot.user.avatar_url)
            await ctx.send (embed = emb)
            print(f'[Logs:info] Информация о категориях команд бота была выведена для пользователя {user} | {prefix}хелп')
        if title != None:
            if title == 'Info' or title == 'info' or title == 'Information' or title == 'information' or title == 'Инфо' or title == 'инфо' or title == 'Информация' or title == 'информация':
                emb = discord.Embed(title = f'Доступные команды группы: `Информация`', description = f'**Префикс: `{prefix}`**', color = defcl['help'])
                emb.add_field(name = f'{prefix}хелп', value = 'Справка по всем команда и их категориям', inline = False)
                emb.add_field(name = f'{prefix}бот', value = 'Информация о боте', inline = False)
                emb.add_field(name = f'{prefix}сервер', value = 'Информация о сервере', inline = False)
                emb.add_field(name = f'{prefix}пинг', value = 'Информация о пинге бота', inline = False)
                emb.add_field(name = f'{prefix}время_работы', value = f'Информация о времени работы бота', inline = False)
                emb.add_field(name = f'{prefix}ресурсы', value = f'Информация о ресурсах бота', inline = False)
                emb.add_field(name = f'Внимание! Если заметили ошибки или недочёты, пожалуйста, опишите их на нашем сервере {links["discord server"]}, будем благодарны!', value = f'Всего команд: {com_value}', inline = False)
                emb.set_thumbnail(url = self.bot.user.avatar_url)
                emb.set_footer(text = copyright_ru, icon_url = self.bot.user.avatar_url)
                await ctx.send (embed = emb)
                print(f'[Logs:info] Информация о категории "Информация" была выведена для пользователя {user} | {prefix}хелп инфо')
            if title == 'Actions' or title == 'actions' or title == 'Action' or title == 'action' or title == 'Действия' or title == 'действия':
                emb = discord.Embed(title = f'Доступные команды группы: `Действия`', description = f'**Префикс: `{prefix}`**', color = defcl['help'])
                emb.add_field(name = f'{prefix}факю', value = 'Послать другого человека', inline = False)
                emb.add_field(name = f'{prefix}увутолк', value = 'Милый разговор >3', inline = False)
                emb.add_field(name = f'{prefix}прессф', value = 'Нажмите F, чтобы отдать респект', inline = False)
                emb.add_field(name = f'{prefix}none', value = 'none', inline = False)
                emb.add_field(name = f'{prefix}none', value = 'none', inline = False)
                emb.add_field(name = f'Внимание! Если заметили ошибки или недочёты, пожалуйста, опишите их на нашем сервере {links["discord server"]}, будем благодарны!', value = f'Всего команд: {com_value}', inline = False)
                emb.set_thumbnail(url = self.bot.user.avatar_url)
                emb.set_footer(text =copyright_ru, icon_url = self.bot.user.avatar_url)
                await ctx.send (embed = emb)
                print(f'[Logs:info] Информация о категории "Действия" была выведена для пользователя {user} | {prefix}хелп действия')
            if title == 'Funny' or title == 'funny' or title == 'Fun' or title == 'fun' or title == 'Весёлое' or title == 'весёлое':
                emb = discord.Embed(title = f'Доступные команды группы: `Весёлое`', description = f'**Префикс: `{prefix}`**', color = defcl['help'])
                emb.add_field(name = f'{prefix}none', value = 'none', inline = False)
                emb.add_field(name = f'{prefix}none', value = 'none', inline = False)
                emb.add_field(name = f'{prefix}none', value = 'none', inline = False)
                emb.add_field(name = f'{prefix}none', value = 'none', inline = False)
                emb.add_field(name = f'{prefix}none', value = 'none', inline = False)
                emb.add_field(name = f'Внимание! Если заметили ошибки или недочёты, пожалуйста, опишите их на нашем сервере {links["discord server"]}, будем благодарны!', value = f'Всего команд: {com_value}', inline = False)
                emb.set_thumbnail(url = self.bot.user.avatar_url)
                emb.set_footer(text = copyright_ru, icon_url = self.bot.user.avatar_url)
                await ctx.send (embed = emb)
                print(f'[Logs:info] Информация о категории "Весёлое" была выведена для пользователя {user} | {prefix}хелп весёлое')
            if title == 'Utilities' or title == 'utilities' or title == 'Util' or title == 'util' or title == 'Utils' or title == 'utils' or title == 'Утилиты' or title == 'утилиты' or title == 'Утил' or title == 'утил' or title == 'Утилс' or title == 'утилс':
                emb = discord.Embed(title = f'Доступные команды группы: `Утилиты`', description = f'**Префикс: `{prefix}`**', color = defcl['help'])
                emb.add_field(name = f'{prefix}аватар', value = 'Показать аватар участника', inline = False)
                emb.add_field(name = f'{prefix}рандом', value = 'Получить рандомное число', inline = False)
                emb.add_field(name = f'{prefix}тайм', value = 'Показывает текущее время по МСК', inline = False)
                emb.add_field(name = f'{prefix}вики', value = 'Выводит искомую информацию с википедии', inline = False)
                emb.add_field(name = f'{prefix}ачивка', value = 'Показывает майнкрафт достижение с вашим текстом', inline = False)
                emb.add_field(name = f'{prefix}реверс', value = 'Реверс текста в обратную сторону', inline = False)
                emb.add_field(name = f'{prefix}ру_раскладка', value = 'Переводит текст на русскую раскладку', inline = False)
                emb.add_field(name = f'{prefix}транслит', value = 'Переводит текст из транслита в русские слова', inline = False)
                emb.add_field(name = f'Внимание! Если заметили ошибки или недочёты, пожалуйста, опишите их на нашем сервере {links["discord server"]}, будем благодарны!', value = f'Всего команд: {com_value}', inline = False)
                emb.set_thumbnail(url = self.bot.user.avatar_url)
                emb.set_footer(text = copyright_ru, icon_url = self.bot.user.avatar_url)
                await ctx.send (embed = emb)
                print(f'[Logs:info] Информация о категории "Утилиты" была выведена для пользователя {user} | {prefix}хелп утилиты')
def setup(bot):
    bot.add_cog(Help(bot))