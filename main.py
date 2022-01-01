import discord
from discord import member
from discord.ext import commands
import json
import random
import os

#open Json file
with open('setting.json','r',encoding='utf8') as ifile:
    idate = json.load(ifile)

bot = commands.Bot(command_prefix="!",intents = discord.Intents.all())

@bot.event
async def on_member_join(member):
	channel = bot.get_channel(int(idate['welcome']))
	await channel.send(f'{member.mention}welcome')

#member_remove
@bot.event
async def on_member_remove(member):
	channel = bot.get_channel(int(idate['leave']))
	await channel.send(f'{member}sad for his remove')

@bot.command()
async def load(ctx, extension):
	bot.load_extension(f'cmds.{extension}')
	await ctx.send(f'load {extension} successful')

@bot.command()
async def unload(ctx, extension):
	bot.unload_extension(f'cmds.{extension}')
	await ctx.send(f'Un - load {extension} successful')

@bot.command()
async def reload(ctx, extension):
	bot.load_extension(f'cmds.{extension}')
	await ctx.send(f'RE - load {extension} successful')



#online event
@bot.event
async def on_ready():
    print('Bot is online')

for filename in os.listdir('./cmds'):
	if filename.endswith('.py'):
		bot.load_extension(f'cmds.{filename[:-3]}')

if __name__ == "__main__":
	bot.run(idate['TOKEN'])
