import discord
from discord.ext import commands
import json
import os


class lvl(commands.Cog):
    def __init__(self, client):
        self.client = client

    

    '''@commands.Cog.listener()
    async def on_ready(self):
        print("Level imported")

    @commands.Cog.listener()
    async def on_member_join(self, member):
        with open('index.json', 'r') as f:
            users = json.load(f)

        await self.update_data(users, member)

        with open('index.json', 'w') as f:
            json.dump(users, f)

    @commands.Cog.listener()
    async def on_message(self, message):

        if message.author == self.client.user:
            return

        with open('index.json', 'r') as f:
            users = json.load(f)

        await self.update_data(users, message.author)
        await self.add_experience(users, message.author, 5)
        await self.level_up(users, message.author, message.channel)

        with open('index.json', 'w') as f:
            json.dump(users, f)

    async def update_data(self, users, user):
        if not str(user.id) in users:
            users[user.id] = {}
            users[user.id]['experience'] = 0
            users[user.id]['level'] = 1

    async def add_experience(self, users, user, exp):
        users[user.id]["experience"] += exp
        
    async def level_up(self, users, user, channel):
        experience = users[user.id]['experience']
        lvl_start = users[user.id]['level']
        lvl_end = int(experience ** (1/4))

        if lvl_start < lvl_end:
            await channel.send(f'{user.mention} levelled up to {lvl_end}')
            users[user.id]['level'] = lvl_end'''


def setup(client):
    client.add_cog(lvl(client))