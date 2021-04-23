# Standard Library Imports
import asyncio
import os

# Third Party Imports
import discord
from discord.ext import commands
from database.databaseHandler import DatabaseHandler
from decouple import config

# Local Application Imports
from cog.cogs import CogHandler
import keep_alive


class MyBot(commands.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.databaseHandler = DatabaseHandler(self)
        self.cogHandler = CogHandler(self)

    async def on_ready(self):
        print(f'Logged in as {myBot.user.name} (ID: {myBot.user.id})')
        print('-------')
        await self.cogHandler.addCogs()

    def add_cog(self, cog: commands.Cog):
        super().add_cog(cog)


myBot = MyBot(("!", "$"))

# keep_alive.keep_alive()

# myBot.run(os.getenv('TOKEN'))

myBot.run(config("TOKEN"))
