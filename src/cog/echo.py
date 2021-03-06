# Standard Library Imports

# Third Party Imports
import discord
from discord.ext import commands
import logging

# Local Application Imports
import wrapper

name = "echo"
aliases = ("repeat", )
helpMessage = "Type after the command and the bot will repeat it"
briefMessage = "I'll repeat one word"

nameT = "talk"
aliasesT = ("TALK",)
helpMessageT = ('Type after the command'
                'and the bot will erase your original message and repeat the message for you ')
briefMessageT = "I'll be angry for you!"


class Echo(commands.Cog):
    def __init__(self, handler):
        self.wrapper = wrapper.Wrapper()
        self.handler = handler
        logging.info("Echo Cog Ready")

    @commands.command(name=name, aliases=aliases, help=helpMessage, brief=briefMessage)
    async def echo_command(self, ctx, *, message: str):
        finalMessage = self.wrapper.AllAngryWrapper(message+'!')
        await ctx.send(f'{self.wrapper.BackQuoteWrapper(finalMessage)}')

    @commands.command(name=nameT, aliases=aliasesT, help=helpMessageT, brief=briefMessageT)
    async def talk_command(self, ctx, *, message: str):
        finalMessage = self.wrapper.AllAngryWrapper(message+'!')
        await ctx.message.delete()
        await ctx.send(f'{self.wrapper.BackQuoteWrapper(finalMessage)}')
