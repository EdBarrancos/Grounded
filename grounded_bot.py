import keep_alive
import asyncio
import discord
import os
from discord.ext import commands
from database.databaseHandler import DatabaseHandler

from decouple import config


class Echo(commands.Cog):
    def _init_(self, bot):
        self.bot = bot
        print("Echo Cog Ready")

    @commands.command(name="echo")
    async def echo_command(self, ctx, message: str):
        await ctx.send(message)


class MyBot(commands.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        databaseHandler = DatabaseHandler(self)

    async def on_ready(self):
        print(f'Logged in as {myBot.user.name} (ID: {myBot.user.id})')
        print('-------')

    def add_cog(self, cog: commands.Cog):
        super().add_cog(cog)


myBot = MyBot(("!", "$"))

myBot.add_cog(Echo(myBot))

# keep_alive.keep_alive()

# myBot.run(os.getenv('TOKEN'))

myBot.run(config("TOKEN"))
