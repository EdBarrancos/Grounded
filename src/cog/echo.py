# Standard Library Imports

# Third Party Imports
import discord
from discord.ext import commands
import logging

# Local Application Imports
import wrapper

name = "echo"
aliases = ("repeat", )
helpMessage = "I'll repeat Whatever You want me to, but just one word, So watchout!"
briefMessage = "I'll repeat one word"

class Echo(commands.Cog):
    def __init__(self, handler):
        self.wrapper = wrapper.Wrapper()
        self.handler = handler
        logging.info("Echo Cog Ready")

    @commands.command(name=name, aliases=aliases, help=helpMessage,brief=briefMessage)
    async def echo_command(self, ctx, *, message: str):
        finalMessage = self.wrapper.AllAngryWrapper(message+'!')
        await ctx.send(f'{self.wrapper.BackQuoteWrapper(finalMessage)}')
