from asyncio.windows_events import NULL
import typing
import discord
from discord.errors import Forbidden
from discord.ext import commands
import json
from discord.ext.commands.errors import MissingPermissions

class mod(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.client.swears = False
        self.client.swearList = ['nig', 'nazi', 'nigger', 'nigga', 'fag', 'neg', 'n1g', 'naz1', 'f@g', 'fag', 'nig', 'nazi', 'fag', 'retard', 'coon', 'c00n', 'coon', 'h3ll', 'retard', 'c-u-n-t', 'cunt', 'cunt', 'n-i-g', 'f-a-g', 'f-@-g', 'fuc', 'shit', 's-h-i-t', 'shit', 'sh1t', 'fuc', 'f-u-c', 'f-uc', 'fu-c', 'a-s-s', 'a-ss', 'as-s', 'a$$', '@ss', 'as$', 'a$s', 'a-$$', 'dild', 'dild', 'd-i-l-d', 'd-i-ld', 'd-ild', 'dil-d', 'r@pe', 'rap3', 'rape', 'r4pe', 'r4p3', 'rape', 'r-a-p-e', 'rap-e', 'dick', 'd1ck', 'dicck', 'd-i-c-k', 'dick', 'dick', 'd-ick', 'd-1ck', 'd1c', 'porn', 'p0rn', 'porn', 'p-o-r-n', 'f.u.c.k', 'n.i.g', 'n_i_g', 'mothafu', 'mothafu', 'onecuptwo', 'onecupone', 'oneguyone', 'oneguytwo', 'peg', 'p3g', 'p-3-g', 'p3-g', 'penis', 'p3n1s', 'penis', 'p.e.n.i.s', 'p.3.n.i.s', 'p3.nis', 'kys', 'killyourself', 'kilyourself', 'hopeyoudie', 'commitsuicide', 'wh0r', 'whor3', 'whore', 'w-h-o-r-e', 'whore', 'wh-ore', 'w-hor3', 'w_h_o_r_e', 'h03', 'ho3', 'hoe', 'h0e', 'hoe', 'h_o_e', 'h.o.e', 'h.o_e', 'h_o.e', 'slut', 's-l-u-t', 'slut', 's_l_u_t', 's.l.u.t', 'slut', 'stfu', 'tw4t', 'twat', 'twat', 'tw4t', 't-w-a-t', 't-w-4-t', 'twat', 't.w.a.t', 't_w_a_t', 't_w_4_t', 'tw@t', 'twat', 'x-rated', 'xrated', '18+', '5h1t', 'anal', '4n4l', 'boob', 'b00b', 'b!tch', 'b17ch', 'gore', 'gor3', 'g0r3', 'g0re', 'c.0.c.k', 'c0ck', 'cock', 'childp', 'childfu', 'cocaine', 'heroine', 'cum', 'c-u-m', 'cum', 'deepthro', 'd33pthr0', 'd33pthro', 'deepthr0', 'molly', 'lsd', 'mdma', 'xanax', 'x4nax', 'xan4x', 'x4n4x', 'ketamine', 'k3t4m', 'ketam', 'k3tam', 'specialk', 'magicshroom', 'marijuana', 'methamphetamine', 'meth', 'm3th', 'smokecrank', 'fentanyl', 'morphine', 'amytal', 'suckmy', 'lickmy', 'gagmy', 'blowmy', 'fag', 'fag', 'nig', 'nig', 'kanker', 'tering', 'debiel', 'mongool', 'tyfus', 'siktir', 'joder', 'zorra', 'pendejo', 'arse', 'idiot', 'sukkel', 'id1ot', '1diot', '1d1ot', 'idi0t', 'id10t', 'vagina', 'shi', 'sh1', '5h', 'uck', '4hit']


    @commands.Cog.listener()
    async def on_ready(self):
        print("Mod imported")

    @commands.Cog.listener()
    async def on_message(self, message):
        if self.client.swears == True:
            for j in self.client.swearList:
                if str(message.content).lower().count(j) > 0:                
                    print(message.content)
                    em = discord.Embed(description = f'{message.author.mention} was warned!')
                    await message.channel.send(embed = em)
                    await message.delete()
                    break

    @commands.command(aliases = ['antiswears'])
    async def antiswear(self, ctx, mode:str):
        """Deletes messages with vulgar language."""
        if ctx.author.guild_permissions.administrator == True:
            try:
                if mode == 'enable':
                    self.client.swears = True
                    await ctx.channel.send('Anti Swear mode Enabled!')
                elif mode == 'disable':
                    self.client.swears = False
                    await ctx.channel.send('Anti Swear mode Disabled!')
                else:
                    await ctx.channel.send('Not Valid.')
            except:
                await ctx.channel.send('Not Valid.')
        else:
            await ctx.channel.send("You're not an admin.")

    @commands.command()
    async def delete(self, ctx, amount: typing.Union[int, float, str]):
        """Single delete or bulk delete messages."""
        if ctx.author.guild_permissions.administrator == True:
            if isinstance(amount, int):
                await ctx.channel.purge(limit = int(amount)+1)
            else:
                await ctx.channel.send("Please provide an integer value.")
        else:
            await ctx.channel.send("You're not an admin.")

    @commands.command()
    async def kick(self, ctx, member: discord.Member, *, reason = None):
        """Kicks the mentioned user with provided reason."""
        if ctx.author.guild_permissions.administrator == True:
            try:
                await member.kick(reason=reason)
                await ctx.channel.send(f'{member.display_name} was kicked!')
            except Forbidden:
                await ctx.channel.send("Nice Try.")
        else:
            await ctx.channel.send("You're not an admin.")

    @commands.command(hidden = True)
    async def leave_server(self, ctx, *, guild_id):
        if ctx.author.id == 485123430010585101:
            for guild in self.client.guilds:
                print(guild.name, guild.id)
            try:
                id_leave = int(guild_id)
            except:
                print('poo')
            server = self.client.get_guild(id_leave)
            await server.leave()
            await ctx.send(f"Left server: {server.name}")
            

    

def setup(client):
    client.add_cog(mod(client))