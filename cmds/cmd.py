import discord
from discord import member
from discord.ext import commands
import json
import random
from core.classes import Cog_Extension

with open('setting.json','r',encoding='utf8') as ifile:
    idate = json.load(ifile)

class Cmd(Cog_Extension):

    #Ping
    @commands.command()
    async def ping(self,ctx):
        await ctx.send(f'ping:{round(self.bot.latency*1000)}(ms)')

#image
    @commands.command()
    async def meme(self,ctx):
        image = random.choice(idate['meme_image'])
        await ctx.send(image)

    @commands.command()
    async def gamble(self,ctx):
        random_num = random.randint(0, 100)
        await ctx.send(f'random:{random_num}')

def setup(bot):
    bot.add_cog(Cmd(bot))
