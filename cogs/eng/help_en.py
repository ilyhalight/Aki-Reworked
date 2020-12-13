import discord
from discord.ext import commands
import config
from config import cogs_color, other_settings, fast_link
from useful import prefix, copyright_en
com_value = other_settings['COMMAND VALUE']
class Help(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases = ['Help', 'help', 'Хелп', 'хелп'])
    async def __help(self, ctx, *, title = None):
        user = ctx.message.author
        if title == None:
            emb = discord.Embed(title = f'Available commands:', description = f'**Prefix: `{prefix}`**', color = cogs_color['HELP NONE COLOR'])
            emb.add_field(name = f'Information ({prefix}help Information)', value = f'`This section contains all information commands`', inline = False)
            emb.add_field(name = f'Moderation ({prefix}ahelp)', value = f'`This section contains all the admin commands`', inline = False)
            emb.add_field(name = f'Actions ({prefix}help Actions)', value = f'`This section contains all RP commands`', inline = False)
            emb.add_field(name = f'Funny ({prefix}help Funny)', value = f'`This section contains all the fun commands`', inline = False)
            emb.add_field(name = f'Utilities ({prefix}help Utilities)', value = f'`This section contains all the utilities`', inline = False)
            emb.add_field(name = f'Attention! If you notice any mistakes or shortcomings, please describe it in our server {fast_link["DISCORD URL"]}, we will be grateful!', value = f'Total commands: {com_value}', inline = False)
            emb.set_thumbnail(url = self.bot.user.avatar_url)
            emb.set_footer(text = copyright_en, icon_url = self.bot.user.avatar_url)
            await ctx.send (embed = emb)
            print(f'[Logs:info] Информация о категориях команд бота выведена для пользователя {user} | {prefix}help')
        if title != None:
            if title == 'Info' or title == 'info' or title == 'Information' or title == 'information' or title == 'Инфо' or title == 'инфо' or title == 'Информация' or title == 'информация':
                emb = discord.Embed(title = f'Available group commands: `Information`', description = f'**Prefix: `{prefix}`**', color = cogs_color['HELP COLOR'])
                emb.add_field(name = f'{prefix}help', value = f'Help for all commands and their categories', inline = False)
                emb.add_field(name = f'{prefix}bot', value = f'Bot information', inline = False)
                emb.add_field(name = f'{prefix}server', value = f'Server information', inline = False)
                emb.add_field(name = f'{prefix}ping', value = f'Bot ping information', inline = False)
                emb.add_field(name = f'{prefix}uptime', value = f'Bot uptime information', inline = False)
                emb.add_field(name = f'{prefix}analytics', value = f'Bot resource information', inline = False)
                emb.add_field(name = f'Attention! If you notice any mistakes or shortcomings, please describe it in our server {fast_link["DISCORD URL"]}, we will be grateful!', value = f'Total commands: {com_value}', inline = False)
                emb.set_thumbnail(url = self.bot.user.avatar_url)
                emb.set_footer(text = f'{copyright_en}', icon_url = self.bot.user.avatar_url)
                await ctx.send (embed = emb)
                print(f'[Logs:info] Информация о категории "Информация" была выведена для пользователя {user} | {prefix}help info')
            if title == 'Actions' or title == 'actions' or title == 'Action' or title == 'action' or title == 'Действия' or title == 'действия':
                emb = discord.Embed(title = f'Available group commands: `Actions`', description = f'**Prefix: `{prefix}`**', color = cogs_color['HELP COLOR'])
                emb.add_field(name = f'{prefix}fucku', value = f'Send the fuck', inline = False)
                emb.add_field(name = f'{prefix}uwutalk', value = f'Uwutalk >3', inline = False)
                emb.add_field(name = f'{prefix}pressf', value = f'Press F to pay respect', inline = False)
                emb.add_field(name = f'{prefix}none', value = f'none', inline = False)
                emb.add_field(name = f'{prefix}none', value = f'none', inline = False)
                emb.add_field(name = f'Attention! If you notice any mistakes or shortcomings, please describe it in our server {fast_link["DISCORD URL"]}, we will be grateful!', value = f'Total commands: {com_value}', inline = False)
                emb.set_thumbnail(url = self.bot.user.avatar_url)
                emb.set_footer(text = copyright_en, icon_url = self.bot.user.avatar_url)
                await ctx.send (embed = emb)
                print(f'[Logs:info] Информация о категории "Действия" была выведена для пользователя {user} | {prefix}help actions')
            if title == 'Funny' or title == 'funny' or title == 'Fun' or title == 'fun' or title == 'Весёлое' or title == 'весёлое':
                emb = discord.Embed(title = f'Available group commands: `Funny`', description = f'**Prefix: `{prefix}`**', color = cogs_color['HELP COLOR'])
                emb.add_field(name = f'{prefix}none', value = f'none', inline = False)
                emb.add_field(name = f'{prefix}none', value = f'none', inline = False)
                emb.add_field(name = f'{prefix}none', value = f'none', inline = False)
                emb.add_field(name = f'{prefix}none', value = f'none', inline = False)
                emb.add_field(name = f'{prefix}none', value = f'none', inline = False)
                emb.add_field(name = f'Attention! If you notice any mistakes or shortcomings, please describe it in our server {fast_link["DISCORD URL"]}, we will be grateful!', value = f'Total commands: {com_value}', inline = False)
                emb.set_thumbnail(url = self.bot.user.avatar_url)
                emb.set_footer(text = copyright_en, icon_url = self.bot.user.avatar_url)
                await ctx.send (embed = emb)
                print(f'[Logs:info] Информация о категории "Весёлое" была выведена для пользователя {user} | {prefix}help fun')
            if title == 'Utilities' or title == 'utilities' or title == 'Util' or title == 'util' or title == 'Utils' or title == 'utils' or title == 'Утилиты' or title == 'утилиты' or title == 'Утил' or title == 'утил' or title == 'Утилс' or title == 'утилс':
                emb = discord.Embed(title = f'Available group commands: `Utilities`', description = f'**Prefix: `{prefix}`**', color = cogs_color['HELP COLOR'])
                emb.add_field(name = f'{prefix}avatar', value = f'Show member avatar', inline = False)
                emb.add_field(name = f'{prefix}rand', value = f'Get a random number', inline = False)
                emb.add_field(name = f'{prefix}time', value = f'Shows the current time by CET', inline = False)
                emb.add_field(name = f'{prefix}wiki', value = f'Displays the information you are looking for from Wikipedia', inline = False)
                emb.add_field(name = f'{prefix}achievement', value = f'Shows minecraft achievement with your text', inline = False)
                emb.add_field(name = f'{prefix}reverse', value = f'Reverse text', inline = False)
                emb.add_field(name = f'{prefix}ru_layout', value = f'Translates text into Russian layout', inline = False)
                emb.add_field(name = f'{prefix}translit', value = f'Translates text from transliteration into Russian words', inline = False)
                emb.add_field(name = f'Attention! If you notice any mistakes or shortcomings, please describe it in our server {fast_link["DISCORD URL"]}, we will be grateful!', value = f'Total commands: {com_value}', inline = False)
                emb.set_thumbnail(url = self.bot.user.avatar_url)
                emb.set_footer(text = copyright_en, icon_url = self.bot.user.avatar_url)
                await ctx.send (embed = emb)
                print(f'[Logs:info] Информация о категории "Утилиты" была выведена для пользователя {user} | {prefix}help utils')
def setup(bot):
    bot.add_cog(Help(bot))