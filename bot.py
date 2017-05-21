import discord 
from discord.ext.commands import Bot 
import asyncio 
import logging 
import config
import random
import datetime
import time
from discord.ext import commands
import platform
import webbrowser
import hashlib
import argparse
import shutil
import stat
import time
import os
import sys
import subprocess
import random
import discord
from discord.ext import commands
from random import randint
from random import choice
from enum import Enum
from urllib.parse import quote_plus
import datetime
import time
import aiohttp
import asyncio

    
logging.basicConfig(level=logging.INFO) # Configurates the logger
logger = logging.getLogger('discord')

description = '''DiscordBot-Launcher a bot made by Articuno & Neo'''

bot = Bot(command_prefix=config.PREFIX) # Sets the client and sets the prefix to what is defined in "config.py"

@bot.event
async def on_ready(): # On the ready event ( CMD OPEN And LOGED)
    users = len(set(bot.get_all_members()))
    servers = len(bot.servers)
    channels = len([c for c in bot.get_all_channels()])
    messages = ["https://discord.gg/6fC3gjm", "https://discord.gg/Ank8Udt", "https://discord.gg/ZBX2qCv", "https://discord.gg/zZjG9pe"]
    print("\n")
    print("\n")
    print("\n")
    print("\n")
    print("\n")
    print("\n")
    print("\n")
    print("\n")
    print("\n")
    print("\n")
    print("\n")
    print("\n")
    print("\n")
    print("\n")
    print("\n")
    print("\n")
    print("\n")
    print("\n")
    print("\n")
    print("\n")
    print("\n")
    print("\n")
    print("\n")
    print("\n")
    print("\n")
    print("\n")
    print('--------------------\n'
          'DiscordBot-Launcher\n'
          '--------------------\n')
    print(bot.user.name)
    print("\n")
    print("Stats:\n")
    print("{} Servers".format(servers))
    print("{} Users".format(users))
    print("{} Channels".format(channels))
    print("Owner: " + config.OWNER)
    print("\n")
    print("Invite : https://discordapp.com//oauth2/authorize?client_id={}&scope=bot&permissions=0".format(bot.user.id))
    print("\n")
    print("Our Offical server : https://discord.gg/U7p7Szs")
    print("Random Server {} want your server mentioned? ask the staff on the offical server!".format(random.choice(messages)))
    print("=========================================================================================\n"
          "Fixed commands! | adding more commands soon!\n"
          "=========================================================================================\n")
    


@bot.command(pass_context=True)
async def info(ctx):
    """Shows information on this bot."""
    await bot.say("**{}** Info\n"
                  "=============\n"
                  "**`Owner` {}**\n **`Staff` {}** ".format(bot.user.name, config.OWNER, config.STAFF))

@bot.command(pass_context=True)
async def serverinfo(ctx):
    """Shows info about the server"""
    server = ctx.message.server
    total_users = len(server.members)
    text_channels = len([x for x in server.channels
                             if x.type == discord.ChannelType.text])
    voice_channels = len(server.channels) - text_channels
    await bot.say("{} Info\n"
                  "=============\n"
                  "Channels | {}\n"
                  "\n"
                  "user count | {}\n".format(server, text_channels, total_users))
bot.run(config.TOKEN)
