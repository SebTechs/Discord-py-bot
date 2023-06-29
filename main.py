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

#Configurations

color = 0xff00ff


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
async def pp(ctx, user: discord.User = None):
    length = random.randint(1,12)
    embed = discord.Embed(colour=color)
    embed.set_footer(text= f"Requested by: {ctx.message.author}")
    if user == None:
        user = ctx.message.author
    else:
        user = user.name
    embed.add_field(name = f"{user} has a...", value=f"{length}inch penis", inline=False)
    await ctx.reply(embed = embed)


@client.command(name = "test")
async def test(ctx):
    message = await ctx.send("I have a 10 inch dick... ")
    await asyncio.sleep(2)
    await message.edit(content = "I have a 10 inch dick... when it's soft")

client.run('MTEyMzk3MTE3MTg4NTUxNDgzMw.Gw6KkC.AYUkaiEhwlXqDoSesCFriyk7456ylRiIGGMzMs')
