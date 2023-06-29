import discord

from discord.ext import commands

# In here you must do self.client when refering to the client.

class Fun_Commands(commands.Cog):
    def __int__(self, client):
        self.client = client
    
    @commands.Cog.listener()
    async def on_ready(self):
        print("Fun commands Loaded")
    



async def setup(client):
    await client.add_cog(Fun_Commands(client))