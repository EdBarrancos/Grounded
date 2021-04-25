# Standard Library Imports
import asyncio

# Third Party Imports
import discord
from discord.ext import commands
import logging

# Local Application Imports
import exceptions
from database.databaseHandler import DatabaseHandler
from cog.cogs import CogHandler


class MyBot(commands.Bot):
    def __init__(self, *args, **kwargs):
        logging.info("Intializing Bot...")
        super().__init__(*args, **kwargs)
        logging.info("Bot Initialized Successfully")


    async def on_ready(self):
        print(f'Logged in as {self.user.name} (ID: {self.user.id})')
        print('-------')

        print("Initializing Handlers")

        try:
            logging.info("Database Handler Initializing...")
            self.databaseHandler = DatabaseHandler(self)
        except exceptions.databaseExceptions.DatabaseException as e:
            logging.error(e)
            raise
        except:
            raise
        else:
            logging.info("Database Handler Initialized Successfully")

        try:
            logging.info("Cog Handler Initializing...")
            self.cogHandler = CogHandler(self)
        except:
            raise
        else:
            logging.info("Cog Handler Initialized Successfully")

        try:
            logging.info("Loading Cogs...")
            await self.cogHandler.addCogs()
        except:
            raise
        else:
            logging.info("Cogs Loaded Successfully")

        print("Handlers Initialized")
        print('-------')

        #await self.databaseHandler.RemoveAllGuilds()
        await self.UpdateGuildDatabase()
        #await self.UpdateGuildDatabase()

        return


    async def UpdateGuildDatabase(self):
        logging.info("Updating Database")
        for guild in self.guilds:
            try:
                await self.databaseHandler.AddGuild(guild.id, guild.name, guild.owner_id)
            except exceptions.databaseExceptions.DatabaseException as e:
                logging.error(e)
                raise
            except:
                raise

        logging.info("Updated")


    async def on_guild_join(self, guild):
        logging.info(f'Guild {guild.name} joined')

        try:
            await self.databaseHandler.AddNewGuild(guild.id, guild.name, guild.owner_id)
        except exceptions.databaseExceptions.DatabaseException as e:
            logging.error(e)
            raise
        except:
            raise


    async def on_guild_remove(self, guild):
        logging.info(f'Guild {guild.name} left')

        try:
            await self.databaseHandler.RemoveGuild(guild.id)
        except exceptions.databaseExceptions.DatabaseException as e:
            logging.error(e)
            raise
        except:
            raise


    def add_cog(self, cog: commands.Cog):
        super().add_cog(cog)