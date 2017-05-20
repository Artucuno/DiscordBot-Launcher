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

@commands.command(pass_context=True)
async def info(ctx):
    """Shows information on this bot."""
    owner = config.OWNER
    devs = config.DEVS
    server = "In Progress"
    info = discord.Embed()
    info.description = "This Is In Progress"
    await bot.say(embed=info)

@commands.command(pass_context=True)
async def staff(ctx):
    """Shows The bot's Staff"""
    staff = discord.Embed()
    staff.title = "My Staff Are {}".format(config.STAFF)
    await bot.say(embed=staff)

@commands.command(pass_context=True)
async def help(ctx):
    """Shows This"""
    VERSION = "1.0"
    helpc = discord.Embed(title="__WizBot Help__", description="""
        **info** Shows Information About The Bot
        **staff** Show The Bot's Staff""")
    helpc.set_footer(text="More Commands Will Be Comming Soon , This Is WizBot Version{}".format(VERSION))
    await bot.say(embed=helpc)
    
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
          "Hello Articuno here! in this version commands may not work altho i am trying to\n"
          "fix this! if you want to help me join the offical server!\n")
