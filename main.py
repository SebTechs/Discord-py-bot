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
intents.message_content = True
client = commands.Bot(command_prefix=",", intents= intents)

userIDs = list()
userXP = list()

@client.event
async def on_ready(): #This is on startup
    print("Hellow world I am alive now and working maybe Change innit")
    await client.change_presence(activity=discord.Game(name="idk by im doing someting"))

#Error Handler

@client.event
async def on_command_error(ctx, erorr):
    if isinstance(erorr, CommandNotFound):
        await ctx.send("Oh you naughty thing, this command doesnt exist")
        return
    raise erorr

    
client.remove_command("help")

@client.command(name = "help") 
async def help(ctx): #This is on ",help" command
    await ctx.send("HELP IS NOT FOR YOU")

@client.event
async def on_message(message): #This is on message
    print(f"message from {message.author}: {message.content}")
    
    isInList = False
    i = 0

    for ids in userIDs:
        if (ids == message.author.id):
            isInList = True
            break
        i += 1

    if(isInList == False):
       userIDs.append(message.author.id)
       userXP.append(0)
       i = len(userIDs) - 1

    for letter in message.content:
        userXP[i] += 1

    await client.process_commands(message)

@client.command()
async def ping(ctx): #This is on ",ping" command
    await ctx.send("Pong")

@client.command(name = "list")
async def list(ctx):
    index = 0
    leaderBoard = ""

    for ids in userIDs:
        leaderBoard += f"{client.get_user(userIDs[index])}'s XP Points: {userXP[index]}\n"
        index += 1

    await ctx.send(leaderBoard)

@client.command(name = "help")
async def help(ctx):
    await ctx.send("HELP IS NOT FOR YOU")

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
    
client.run('Token')
