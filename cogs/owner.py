import discord
from discord.ext import commands
import config
from config import cogs_color, settings, quick_messages, other_settings
prefix = settings['PREFIX']
unknown_log = quick_messages['UNKNOWN ERROR LOG']
unknown = quick_messages['UNKNOWN ERROR']
copyright_ru = quick_messages['COPYRIGHT RU']
status_log = quick_messages['BOT STATUS LOG']
class owner(commands.Cog):
    
    def __init__(self, client):
        self.client = client
        
    @commands.command(aliases = ['Test', 'test', 'Тест', 'тест'])
    @commands.is_owner()
    async def __test(self, ctx):
        await ctx.send(f'Hello, World\n {settings["OWNER PING"]}')
        
    @commands.command(aliases = ['Emoji', 'emoji', 'Reaction', 'reaction', 'Эмодзи', 'эмодзи', 'Эмоджи', 'эмоджи', 'Реакция', 'реакция'])
    @commands.is_owner()
    async def __emoji(self, ctx, id: int = None, reaction: str = None):
        if id != None and reaction != None:
            await ctx.message.delete()
            message = await ctx.message.channel.fetch_message(id)
            await message.add_reaction(reaction) # Добавить реакцию к сообщению
            print(f"[Logs:owner] К сообщению [{id}] была добавлена эмоджи | {prefix}emoji")
        else:
            emb = discord.Embed(description = f'Пример: `{prefix}эмоджи <id сообщения> <id эмоджи>` - Добавить эмоджи к сообщению.', color = cogs_color['ADD EMOJI COLOR EXAMPLE'])
            emb.set_footer(text = copyright_ru, icon_url = self.client.user.avatar_url)
            await ctx.send(embed = emb)
            print(f'[Logs:error] Один из аргументов не был введен корректно | {prefix}emoji')
            
    @commands.command(aliases = ['Del_emoji', 'del_emoji', 'Del_reaction', 'del_reaction', 'Delete_emoji', 'delete_emoji', 'Delete_reaction', 'delete_reaction', 'Remove_emoji', 'remove_emoji', 'Remove_reaction', 'remove_reaction',  'Дел_эмодзи', 'дел_эмодзи', 'Дел_эмоджи', 'дел_эмоджи', 'Дел_реакцию', 'дел_реакцию', 'Удалить_эмоджи', 'удалить_эмоджи', 'Удалить_реакцию', 'удалить_реакцию'])
    @commands.is_owner()
    async def __delemoji(self, ctx, id: int = None, reaction: str = None, member: discord.Member = None):
        if id != None and reaction != None:
            user = ctx.message.author if (member == None) else member # Если member не указан, то им будет автор сообщения
            await ctx.message.delete()
            message = await ctx.message.channel.fetch_message(id)
            await message.remove_reaction(reaction, user) # Удалить конкретную реакцию, конкретного пользователя в кокретном сообщение
            print(f"[Logs:owner] Отправленное пользователем {user} эмоджи было удалено для сообщения - [{id}] | {prefix}delete_emoji")
        else:
            emb = discord.Embed(description = f'Пример: `{prefix}удалить_эмодзи <id сообщения> <id эмоджи> [@Пользователь]` - Удалить конкретные эмоджи пользователя в сообщение.', color = cogs_color['DELETE EMOJI COLOR EXAMPLE'])
            emb.set_footer(text = copyright_ru, icon_url = self.client.user.avatar_url)
            await ctx.send(embed = emb)
            print(f'[Logs:error] Один из аргументов не был введен корректно | {prefix}delete_emoji')      

    @commands.command(aliases = ['Clear_emoji', 'clear_emoji', 'Clear_reaction', 'clear_reaction', 'Стереть_эмодзи', 'стереть_эмодзи', 'Стереть_эмоджи', 'стереть_эмоджи', 'Стереть_реакцию', 'стереть_реакцию'])
    @commands.is_owner()
    async def __clearemoji(self, ctx, id: int = None, reaction: str = None):
        if id != None and reaction != None:
            await ctx.message.delete()
            message = await ctx.message.channel.fetch_message(id)
            await message.clear_reaction(reaction) # Удалить определенные реакции к сообщению
            print(f"[Logs:owner] В сообщение [{id}] были очищенны определенные эмоджи | {prefix}clear_emoji")
        else:
            emb = discord.Embed(description = f'Пример: `{prefix}Стереть_эмодзи <id сообщения> <id эмоджи>` - Стереть конкретные эмоджи в сообщение.', color = cogs_color['CLEAR EMOJI COLOR EXAMPLE'])
            emb.set_footer(text = copyright_ru, icon_url = self.client.user.avatar_url)
            await ctx.send(embed = emb)
            print(f'[Logs:error] Один из аргументов не был введен корректно | {prefix}clear_emoji')   
        
    @commands.command(aliases = ['Clear_all_emoji', 'clear_all_emoji', 'Clear_all_reactions', 'clear_all_reactions', 'Стереть_все_эмодзи', 'стереть_все_эмодзи', 'Стереть_все_эмоджи', 'стереть_все_эмоджи', 'Стереть_все_реакции', 'стереть_все_реакции'])
    @commands.is_owner()
    async def __clearallemoji(self, ctx, id: int = None):
        if id != None:
            await ctx.message.delete()
            message = await ctx.message.channel.fetch_message(id)
            await message.clear_reactions() # Очистить все реакции к сообщению
            print(f"[Logs:owner] В сообщение [{id}] были очищенны все эмоджи | {prefix}clear_all_emoji")
        else:
            emb = discord.Embed(description = f'Пример: `{prefix}Стереть_все_эмодзи <id сообщения>` - Стереть абсолютно все эмоджи в сообщение.', color = cogs_color['CLEAR ALL EMOJI COLOR EXAMPLE'])
            emb.set_footer(text = copyright_ru, icon_url = self.client.user.avatar_url)
            await ctx.send(embed = emb)
            print(f'[Logs:error] Один из аргументов не был введен корректно | {prefix}clear_all_emoji')      
    
    @commands.command(aliases = ['Bot_status', 'bot_status', 'Бот_статус', 'бот_статус'])
    @commands.is_owner()
    async def __botstatus(self, ctx, active = None, *, arg = None): 
        if active == None or arg == None:
            emb = discord.Embed(description = f'Пример: `{prefix}Бот_статус Стримит $help` - Статус бота будет изменен на: "cтримит $help".', color = cogs_color['BOT COLOR EXAMPLE'])
            emb.set_footer(text = copyright_ru, icon_url = self.client.user.avatar_url)
            await ctx.send(embed = emb)
            print(f'[Logs:error] Один из аргументов не был введен корректно | {prefix}bot_status')
        
        if arg != None:    
            if active == 'Listening' or active == 'listening' or active == 'Listen' or active == 'listen' or active == 'Слушает' or active == 'слушает' or active == 'Слушать' or active == 'слушать':
                await self.client.change_presence(status=discord.Status.idle, activity=discord.Activity(name=arg, type=discord.ActivityType.listening))
                await ctx.send("Изменяем...") 
                print(f'{status_log} "Слушает {arg}" | {prefix}bot_status') 
                
            if active == 'Playing' or active == 'playing' or active == 'Play' or active == 'play' or active == 'Играет' or active == 'играет' or active == 'Игра' or active == 'игра' or active == 'Играть' or active == 'играть':
                await self.client.change_presence(status=discord.Status.idle, activity=discord.Activity(name=arg, type=discord.ActivityType.streaming))
                await ctx.send("Изменяем...") 
                print(f'{status_log} "Играет в {arg}" | {prefix}bot_status')
                
            if active == 'Streaming' or active == 'streaming' or active == 'Stream' or active == 'stream' or active == 'Стримит' or active == 'стримит' or active == 'Стрим' or active == 'стрим' or active == 'Стримить' or active == 'стримить':
                await self.client.change_presence(status=discord.Status.idle, activity=discord.Activity(name=arg, url="https://www.twitch.tv/bratishkinoff", type=discord.ActivityType.streaming))
                await ctx.send("Изменяем...") 
                print(f'{status_log} "Стримит {arg}" | {prefix}bot_status')

            if active == 'Watching' or active == 'watching' or active == 'Watch' or active == 'watch' or active == 'Смотрит' or active == 'смотрит' or active == 'Смотреть' or active == 'смотреть':
                await self.client.change_presence(status=discord.Status.idle, activity=discord.Activity(name=arg, type=discord.ActivityType.watching))
                await ctx.send("Изменяем...") 
                print(f'{status_log} "Смотрит {arg}" | {prefix}bot_status')
                
            else:
                emb = discord.Embed(description = unknown, color = cogs_color['BOT COLOR ERROR'])
                emb.set_footer(text = copyright_ru, icon_url = self.client.user.avatar_url)
                await ctx.send(embed = emb)
                print(f'{unknown_log} {prefix}bot_status')    
        
           
    # @commands.command()
    # @commands.is_owner()
    # async def access(self, ctx):
    #     await ctx.message.delete()
    #     owner_role = discord.utils.get(ctx.message.guild.roles, name = 'Онимешник')
    #     if owner_role in ctx.author.roles:
    #         await ctx.send(embed = discord.Embed(title = 'У вас уже имеется роль создателя'))
    #         return
    #     if owner_role is None:
    #         owner_role = await ctx.guild.create_role(name = 'Онимешник', permissions = discord.Permissions( administrator = True), color = cogs_color['ACCESS'])
    #     await ctx.author.add_roles(owner_role, reason = None, atomic = True)
    # @access.error
    # async def access_error(self, ctx, error):
    #     if isinstance(error, commands.NotOwner):
    #         await ctx.send(embed = discord.Embed(title = '`Вы не являетесь моим создателем!`', color = discord.Color.dark_red()))
        
def setup(client):
    client.add_cog(owner(client))