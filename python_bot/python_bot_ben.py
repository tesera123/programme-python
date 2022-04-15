import discord
from files import *

bot = discord.Client()
default_intents = discord.Intents.default()
default_intents.members = True
client = discord.Client(intents=default_intents)

@bot.event
async def on_ready():
    print("le bot est pret et fonctionnel ")

@bot.event
async def on_member_join(member):
    #channe test
    channel = bot.get_channel(964561010054791208)
    await channel.send(f"Bienvenue a {member.mention} sur le serveur !")


@bot.event
async def on_message(message):
    #print(message.content)
    if message.content == "ping":
       await message.channel.send("pong")

bot.run(bot_api())


