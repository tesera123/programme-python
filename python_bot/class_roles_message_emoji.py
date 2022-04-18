from files import *
import discord
from discord.ext import commands

client = discord.Client()
client = commands.Bot(command_prefix = "!")

class Myclient(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.target_message_id = 965375310575050752

    async def on_ready(self):
        print("ready")

    async def on_raw_reaction_add(self, payload):
        if payload.message_id != self.target_message_id:
            return
        guild = client.get_guild(payload.guild_id)
        print(payload.emoji.name)
        if payload.emoji.name == '😃':
            role = discord.utils.get(guild.roles, name='emoji 1')
            await payload.member.add_roles(role)
        elif payload.emoji.name == '😎':
            role = discord.utils.get(guild.roles, name='emoji 2')
            await payload.member.add_roles(role)
        elif payload.emoji.name == '😀':
            role = discord.utils.get(guild.roles, name='emoji 3')
            await payload.member.add_roles(role)

    async def on_raw_reaction_remove(self, payload):
        if payload.message_id != self.target_message_id:
            return
        guild = client.get_guild(payload.guild_id)
        member = guild.get_member(payload.user_id)
        print(payload.emoji.name)
        if payload.emoji.name == '😃':
            role = discord.utils.get(guild.roles, name='emoji 1')
            await member.remove_roles(role)
        elif payload.emoji.name == '😎':
            role = discord.utils.get(guild.roles, name='emoji 2')
            await member.remove_roles(role)
        elif payload.emoji.name == '😀':
            role = discord.utils.get(guild.roles, name='emoji 3')
            await member.remove_roles(role)



intents = discord.Intents.default()
intents.members = True
client = Myclient(intents=intents)
client.run(bot_api())


