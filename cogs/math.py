from asyncio.windows_events import NULL
import discord
from discord.ext import commands

class math(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Math imported")

    @commands.command(aliases = ['calc'])
    async def calculate(self, ctx, *, question = ""):
        """Calculates the given expression"""
        print(question)
        if question == "":
            await ctx.channel.send("There is nothing to calculate.")
        else:
            try:
                await ctx.channel.send(f'Answer: {eval(question)}')
            except:
                await ctx.channel.send("That cannot be calculated.")

def setup(client):
    client.add_cog(math(client))
