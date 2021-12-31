import discord
from discord import member
from discord.ext import commands
import json
import random

class Cog_Extension(commands.Cog):
    def __init__(self,bot):
        self.bot = bot