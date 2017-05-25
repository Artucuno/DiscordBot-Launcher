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

def is_git_installed():
    try:
        subprocess.call(["git", "--version"], stdout=subprocess.DEVNULL,
                                              stdin =subprocess.DEVNULL,
                                              stderr=subprocess.DEVNULL)
    except FileNotFoundError:
        return False
    else:
        return True

logging.basicConfig(level=logging.INFO) # Configurates the logger
logger = logging.getLogger('discord')
description = '''DiscordBot-Launcher a bot made by Articuno & Neo'''
bot = Bot(command_prefix=config.PREFIX) # Sets the client and sets the prefix to what is defined in "config.py"
users = len(set(bot.get_all_members()))
servers = len(bot.servers)
channels = len([c for c in bot.get_all_channels()])
messages = ["https://discord.gg/6fC3gjm", "https://discord.gg/Ank8Udt", "https://discord.gg/ZBX2qCv", "https://discord.gg/zZjG9pe"]

def user_choice():
    return input("> ").lower().strip()

def run_bot():
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
    print(config.BOTNAME)
    print("\n")
    print("Stats:\n")
    print("UNKNOWN Servers".format(servers))
    print("UNKNOWN Users".format(users))
    print("UNKNOWN Channels".format(channels))
    print("Owner: " + config.OWNER)
    print("\n")
    print("Invite : https://discordapp.com//oauth2/authorize?client_id={}&scope=bot&permissions=0".format(config.BOTID))
    print("\n")
    print("Our Offical server : https://discord.gg/U7p7Szs")
    print("Random Server {} want your server mentioned? ask the staff on the offical server!".format(random.choice(messages)))
    print("=========================================================================================\n"
          "Errors with startup so it wont show Servers, users or channels! sorry! :(\n")
    print("=========================================================================================\n")
    bot.run(config.TOKEN)

logging.basicConfig(level=logging.INFO) # Configurates the logger
logger = logging.getLogger('discord')

def main():
    print("==========================\n"
          "DiscordBot-Launcher\n"
          "==========================\n")
    print("\n")
    print("1. Run DiscordBot-Launcher")
    print("2. Licence + (c) info")
    print("0. Quit")
    choice = user_choice()
if choice == "1":
    run_bot()
if choice == "2":
    print("{}".format(LICENCE))
    choice = user_choice()
    if choice == "0":
        print("0. back")
        main()
elif choice == "0":
    print("you may now close this terminal!")
    
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

@bot.command(pass_context=True)
async def github(ctx):
    """DiscordBot-Launcher's repo"""
    em = discord.Embed(color=0x0BFCF2)
    em.add_field(name='Link', value=("[Click Here!](https://github.com/Articuno1234/DiscordBot-Launcher)"))
    em.add_field(name='Version', value=config.VERSION)
    em.set_thumbnail(url= "https://assets-cdn.github.comem.add_field(name='Link', value=("[Click Here!]("https://github.com/Articuno1234/DiscordBot-Launcher)")))/images/spinners/octocat-spinner-128.gif")
    await bot.say(embed = em)
    

@bot.command(pass_context=True)
async def ping(ctx):
    """Shows info about the server"""
    t1 = time.perf_counter()
    await bot.send_typing(ctx.message.channel)
    t2 = time.perf_counter()
    await bot.say("**Pong.**\nTime: " + str(round((t2-t1)*1000)) + "ms")

@bot.command(pass_context=True)
async def sysinfo(ctx):
    """"""
    await bot.say("")

    
@bot.command(pass_context=True)
async def req(ctx):
    """checks if requirements are installed"""
    em = discord.Embed(color=0x0BFCF2)
    em.add_field(name=':smile:', value=("Requirements are installed!"))
    await bot.say(embed = em)

@bot.command(pass_context=True)
async def binfo(ctx):
    """This does stuff!"""
    import datetime
    commands_run = bot.counter['processed_commands']
    read_messages = bot.counter['messages_read']
    since = bot.uptime.strftime("%Y-%m-%d %H:%M:%S")
    passed = get_bot_uptime()
    cpu_p = psutil.cpu_percent(interval=None, percpu=True)
    cpu_usage = sum(cpu_p) / len(cpu_p)
    mem_v = psutil.virtual_memory()
    servers = str(len(self.bot.servers))
    users = str(len(set(self.bot.get_all_members())))
    server = ctx.message.server
    text_channels = len([x for x in server.channels
                         if x.type == discord.ChannelType.text])
    voice_channels = len(server.channels) - text_channels
    channels = text_channels + voice_channels
    em = discord.Embed(color=0x8d17f9)
    em.set_author(name='Bot info')
    em.add_field(name='Name', value=(config.BOTNAME))
    em.add_field(name='Commands Run :cloud: ', value=commands_run)
    em.add_field(name='Messages read :eyes: ', value=read_messages)
    em.add_field(name='CPU usage :computer: ', value='{0:.1f}%'.format(cpu_usage))
    em.add_field(name='Memory usage :computer: ', value='{0:.1f}%'.format(mem_v.percent))
    em.add_field(name='Servers :book: ', value=servers)
    em.add_field(name='Users :person_with_blond_hair: ', value=users)
    t1 = time.perf_counter()
    t2 = time.perf_counter()
    em.add_field(name='Ping Time :stopwatch: ', value=("Time: \n"
                                                        "?ms"))
    em.add_field(name='**Channels** :newspaper: ', value=str(channels))
    em.add_field(name='**Server Text channels** :speech_balloon: ', value=str(text_channels))
    em.add_field(name='**Server Voice channels** :speaker: ', value=str(voice_channels))
    em.add_field(name='Uptime', value= passed)
    em.add_field(name='Bot Owner :smile:', value="<@183119845900943360>")
    em.add_field(name='Developers :tools:', value="<@280618116566745088>\n <@131904889843482626>\n <@208642717205397506>\n <@193972602392281088>\n <@223754830747926528>")
    em.add_field(name='Bot Supporters :tools:', value="<@299077221061099530>\n <@254214302653743104>\n <@304887486168039424>\n <@284631037026369536>")
    em.add_field(name='Partners :reminder_ribbon: ', value="<@131904889843482626>\n <@193972602392281088>")
    em.set_footer(text='API version {}'.format(discord.__version__))
    await bot.say(embed = em)
    em = discord.Embed(color=0x8d17f9)
    em.set_author(name='Other Information')
    em.add_field(name='Invite', value=("[Click here!](https://discordapp.com/oauth2/authorize?client_id={}&scope=bot&permissions=-1)".format(config.BOTID)))
    await bot.say(embed = em)

has_git = is_git_installed()
is_git_installation = os.path.isdir(".git")
if not is_git_installation:
            print("THIS HAS NOT BEEN INSTALLED WITH GIT! (updating may not work")
print("==========================\n"
      "DiscordBot-Launcher\n"
      "==========================\n")
print("\n")
print("1. Run DiscordBot-Launcher")
print("2. Licence + (c) info")
print("0. Quit")
choice = user_choice()
if choice == "1":
    run_bot()
if choice == "2":
    print("{}".format(LICENCE))
    choice = user_choice()
    if choice == "0":
        print("0. back")
        print("restart terminal")
elif choice == "0":
    print("you may now close this terminal!")
