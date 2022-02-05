import imp
import discord
from discord.ext import commands
from util import log
from util import mic
import json

class Owner(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.check(mic)
    async def reload(self, ctx, extension):
        self.client.reload_extension(f"cogs.{extension}")
        embed = discord.Embed(title='Reload', description=f'{extension} successfully reloaded', color=0xff00c8)
        await ctx.send(embed=embed)


    @commands.command()
    @commands.check(mic)
    async def load(self, ctx, extension):
        self.client.load_extension(f"cogs.{extension}")
        embed = discord.Embed(title='Load', description=f'{extension} successfully loaded', color=0xff00c8)
        await ctx.send(embed=embed)
    

    @commands.command()
    @commands.check(mic)
    async def unload(self, ctx, extension):
        self.client.unload_extension(f"cogs.{extension}")
        embed = discord.Embed(title='Unload', description=f'{extension} successfully unloaded', color=0xff00c8)
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Owner(client))