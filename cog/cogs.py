# Standard Library Imports

# Third Party Imports
import discord
from discord.ext import commands

# Local Application Imports
from .echo import Echo


class CogHandler():
    def __init__(self, owner):
        self.owner = owner

    async def addCogs(self):
        self.owner.add_cog(Echo(self))
