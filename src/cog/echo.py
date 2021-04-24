# Standard Library Imports

# Third Party Imports
import discord
from discord.ext import commands

# Local Application Imports


class Echo(commands.Cog):
    def _init_(self, bot):
        self.bot = bot
        print("Echo Cog Ready")

    @commands.command(name="echo")
    async def echo_command(self, ctx, message: str):
        await ctx.send(message)
