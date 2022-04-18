import discord
from files import *
from discord.utils import get
intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)

ROLE = "emoji 1"

@client.event
async def on_member_join(member):
    role = get(member.guild.roles, name=ROLE)
    await member.add_roles(role)

client.run(bot_api())