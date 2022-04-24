import discord

import class_roles_message_emoji
import affect_role_if_new_member

from discord.ext import commands
from discord.utils import get

from files import *


client = discord.Client()
client = commands.Bot(command_prefix = "!")

# @client.event
# async def on_ready():
#     print("le bot est pret et fonctionnel ")

affect_role_if_new_member()
class_roles_message_emoji.client_test()

@client.event
async def on_message(message):
    #print(message.content)
    if message.content == "ping":
       await message.channel.send("pong")

client.run(bot_api())


