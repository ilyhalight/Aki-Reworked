import discord
from discord.ext import commands
import os, config
from config import cogs_color, settings
prefix = settings['PREFIX']
class main(commands.Cog):
    
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Ready!')
        print(f'Logged in as ----> {self.client.user.name}')
        print(f'ID: {self.client.user.id}')

    @commands.command()
    @commands.is_owner()
    async def test(self, ctx):
        await ctx.send("Hello, World")
        
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
    client.add_cog(main(client))