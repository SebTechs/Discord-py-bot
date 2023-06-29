import discord
from discord.ext import commands

# In here you must do self.client when refering to the client.

class Help(commands.Cog):
    def __int__(self, client):
        self.client = client
    
    @commands.Cog.listener()
    async def on_ready(self):
        print("Bot is online")
    
    @commands.command()
    async def ping(self, ctx):
        await ctx.send("Pong")
    
async def setup(client):
    await client.add_cog(Help(client))