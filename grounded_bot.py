import keep_alive
import asyncio
import discord
import json
from discord.ext import commands


# import Bot Token
with open('bot_token.json') as json_file:
    data = json.load(json_file)
    TOKEN = data["TOKEN"]

myBot = commands.Bot(('!', '$'))


@myBot.event
async def on_ready():
    print(f'Logged in as {myBot.user.name} (ID: {myBot.user.id})')
    print('-------')


class Echo(commands.Cog):
    def _init_(self, bot):
        self.bot = bot

    @commands.command()
    async def echo(self, ctx, message: str):
        await ctx.send(message)


myBot.add_cog(Echo())
myBot.run(TOKEN)
# keep_alive.keep_alive()
