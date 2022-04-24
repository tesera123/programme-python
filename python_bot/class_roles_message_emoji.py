from files import *
import discord
from discord.ext import commands

client = discord.Client()
intents = discord.Intents.default()
intents.members = True

class client_test(discord.Client):
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

client = client_test(intents=intents)
client.run(bot_api())


