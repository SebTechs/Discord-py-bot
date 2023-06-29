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

#Error Handler

@client.event
async def on_command_error(ctx, erorr):
    if isinstance(erorr, CommandNotFound):
        await ctx.send("Oh you naughty thing, this command doesnt exist")
        return
    raise erorr


#Fun commands

#PP commands (length)
@client.command(name = "pp")
async def pp(ctx):
    length = random.randint(1,300)
    embed = discord.Embed(colour=0xff00ff)
    embed.add_field(name = "You have a...", value=f"{length}inch penis", inline=False)
    embed.set_footer(text= f"Requested by: {ctx.message.author}")
    await ctx.reply(embed = embed)


client.run('MTEyMzk3MTE3MTg4NTUxNDgzMw.G41zuj.A6mDZZ_s2GeVVhSostbFZ3q2up3Slu-KkTeHMo')
