# Standard Library Imports

# Third Party Imports
import discord
from discord.ext import commands
import logging

# Local Application Imports

name = "echo"
aliases = ("repeat", )
helpMessage = "I'll repeat Whatever You want me to, but just one word, So watchout!"
briefMessage = "I'll repeat one word"

class Echo(commands.Cog):
    def _init_(self, handler):
        self.handler = handler
        logging.info("Echo Cog Ready")

    @commands.command(name=name, aliases=aliases, help=helpMessage,brief=briefMessage)
    async def echo_command(self, ctx, *, message: str):
        await ctx.send(f'>{message}!')
