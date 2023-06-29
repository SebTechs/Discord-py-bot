#Python  3.11.3

from asyncio import create_task
import asyncio
from datetime import datetime
from operator import truediv
import discord
import random
import os
from discord import *
from discord.ext.commands import CommandNotFound, Bot, errors, guild_only
import time
from discord.ext import commands 

intents = discord.Intents.all()
client = commands.Bot(command_prefix=",", intents= intents)
@client.event
async def on_ready():
    print("Hellow world I am alive now and working maybe Change innit")
    await client.change_presence(activity=discord.Game(name="idk by im doing someting"))

client.remove_command("help")
@client.command(name = "help")
async def help(ctx):
    await ctx.send("HELP IS NOT FOR YOU")


client.run('MTEyMzkyOTk5NjAwNDY4Nzk4Mw.GPNVut.o6S12WXCc0bInFQhM_Fn9ZMGBCVKDPhIsh7F4Y')
