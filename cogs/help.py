import discord
import random
from discord.ext import commands

# In here you must do self.client when refering to the client.


class Help(commands.Cog):
    def __int__(self, client):
        self.client = client
    
    @commands.Cog.listener()
    async def on_ready(self):
        print("Help commands loaded")
    
    @commands.command()
    async def pp(self, ctx):
        length = random.randint()
        await ctx.send("No")
        print("wtf")
    
async def setup(client):
    await client.add_cog(Help(client))