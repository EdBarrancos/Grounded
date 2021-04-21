import keep_alive
import asyncio
import discord
import json


# import Bot Token
with open('bot_token.json') as json_file:
    data = json.load(json_file)
    TOKEN = data["TOKEN"]

keep_alive.keep_alive()
