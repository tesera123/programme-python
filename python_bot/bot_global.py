from files import *
import discord
from discord.ext import commands
from discord.utils import get

client = discord.Client()
client = commands.Bot(command_prefix = "!")

# @client.event
# async def on_ready():
#     print("le bot est pret et fonctionnel ")
ROLE = "role de bienvenue"

@client.event
async def on_member_join(member):
    role = get(member.guild.roles, name=ROLE)
    await member.add_roles(role)

class Myclient(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.target_message_id = 965723572876222585

    async def on_ready(self):
        print("ready")

    async def on_raw_reaction_add(self, payload):
        if payload.message_id != self.target_message_id:
            return
        guild = client.get_guild(payload.guild_id)
        print(payload.emoji.name)
        if payload.emoji.name == '🔞': 
            role = discord.utils.get(guild.roles, name='+18')
            await payload.member.add_roles(role)
        elif payload.emoji.name == '😎':
            role = discord.utils.get(guild.roles, name='gens contents')
            await payload.member.add_roles(role)
        elif payload.emoji.name == '😡':
            role = discord.utils.get(guild.roles, name='hyper actif')
            await payload.member.add_roles(role)
        elif payload.emoji.name == '🆗':
            role = discord.utils.get(guild.roles, name='role de bienvenue')
            await payload.member.remove_roles(role)

    async def on_raw_reaction_remove(self, payload):
        if payload.message_id != self.target_message_id:
            return
        guild = client.get_guild(payload.guild_id)
        member = guild.get_member(payload.user_id)
        print(payload.emoji.name)
        if payload.emoji.name == '🔞':
            role = discord.utils.get(guild.roles, name='+18')
            await member.remove_roles(role)
        elif payload.emoji.name == '😎':
            role = discord.utils.get(guild.roles, name='gens contents')
            await member.remove_roles(role)
        elif payload.emoji.name == '😡':
            role = discord.utils.get(guild.roles, name='hyper actif')
            await member.remove_roles(role)

intents = discord.Intents.default()
intents.members = True
client = Myclient(intents=intents)

@client.event
async def on_message(message):
    #print(message.content)
    if message.content == "ping":
       await message.channel.send("pong")

client.run(bot_api())


