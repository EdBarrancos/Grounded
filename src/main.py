# Standard Library Imports
import asyncio
import logging
import os

# Third Party Imports
import discord
from decouple import config

# Local Application Imports
import keep_alive
from grounded_bot import MyBot


logging.basicConfig(format='%(levelname)s:%(message)s', 
                    filename="bot_logs/grounded_bot.log", 
                    level=logging.INFO, filemode="w")

intents = discord.Intents.default()
intents.members = True

myBot = MyBot(("!", "$"), intents=intents)

# keep_alive.keep_alive()

# myBot.run(os.getenv('TOKEN'))

myBot.run(config("TOKEN"))
