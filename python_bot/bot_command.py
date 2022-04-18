from discord.ext import commands
from files import *

bot = commands.Bot(command_prefix = "!")

#explication des commandes : https://www.youtube.com/watch?v=-WbEpr-qtW8

@bot.command()
async def punch(ctx,arg1):
    await ctx.send(f'Punched {arg1}')


@bot.command()
async def info(ctx):
    await ctx.send(ctx.guild)
    await ctx.send(ctx.author)
    await ctx.send(ctx.message.id)
    


bot.run(bot_api())