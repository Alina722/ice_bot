import discord
from discord import member
from discord.ext import commands
import json
import random

#open Json file
with open('setting.json','r',encoding='utf8') as ifile:
    idate = json.load(ifile)

bot = commands.Bot(command_prefix="!",intents = discord.Intents.all())

#online event
@bot.event
async def on_ready():
    print('Bot is online')

#member_join
@bot.event
async def on_member_join(member):
  channel = bot.get_channel(int(idate['bot_work_factory_welcome']))
  await channel.send(f'{member.mention}welcome')

#member_remove
@bot.event
async def on_member_remove(member):
  channel = bot.get_channel(int(idate['']))
  await channel.send(f'{member}sad for his remove')

#Ping
@bot.command()
async def ping(ctx):
  await ctx.send(f'ping::{round(bot.latency*1000)}(ms)')

#image
@bot.command()
async def meme(ctx):
  image = random.choice(idate['meme_pic'])
  await ctx.send(image)

@bot.command()
async def gamble(ctx):
  random_num = random.randint(0, 100)
  await ctx.send(f'random:{random_num}')


bot.run(idate['TOKEN'])
