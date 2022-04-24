from discord.ext import commands
from files import *

import discord

from discord.utils import get
intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)

bot = commands.Bot(command_prefix='$')

@bot.command()
async def test(ctx, arg):
    await ctx.send(arg)


@bot.command()
async def addrole(ctx, user: discord.Member):
    
    guild = ctx.guild # You can remove this if you don't need it for something other
    role = ctx.guild.get_role(965376110781136906)
    await user.add_roles(role)


bot.run(bot_api())