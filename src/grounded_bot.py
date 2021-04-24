# Standard Library Imports
import asyncio
import os

# Third Party Imports
import discord
from discord.ext import commands
import logging
from decouple import config

# Local Application Imports
import database.databaseHandler as databaseHandler
import cog.cogs as cogs
from database.databaseHandler import DatabaseHandler
from cog.cogs import CogHandler
import keep_alive


class MyBot(commands.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    async def on_ready(self):
        print(f'Logged in as {myBot.user.name} (ID: {myBot.user.id})')
        print('-------')

        try:
            print("Database Initializing...")
            self.databaseHandler = DatabaseHandler(self)
        except databaseHandler.DatabaseError as e:
            print(e)
        else:
            print("Success")

        self.cogHandler = CogHandler(self)
        await self.cogHandler.addCogs()

    async def on_guild_join(self, guild):
        self.databaseHandler.AddServer(guild)

    async def on_guild_remove(self, guild):
        self.databaseHandler.RemoveServer(guild)

    def add_cog(self, cog: commands.Cog):
        super().add_cog(cog)

logging.basicConfig(format='%(levelname)s:%(message)s', filename="bot_logs/grounded_bot.log", level=logging.DEBUG, filemode="w")
myBot = MyBot(("!", "$"))

# keep_alive.keep_alive()

# myBot.run(os.getenv('TOKEN'))

myBot.run(config("TOKEN"))
