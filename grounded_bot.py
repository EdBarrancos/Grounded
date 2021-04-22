import keep_alive
import asyncio
import discord
import os
from discord.ext import commands
from database.databaseHandler import DatabaseHandler


""" @myBot.event
async def on_ready():
    print(f'Logged in as {myBot.user.name} (ID: {myBot.user.id})')
    print('-------')
    databaseHandler = DatabaseHandler(myBot) """


class Echo(commands.Cog):
    def _init_(self, bot):
        self.bot = bot

    @commands.command()
    async def echo(self, ctx, message: str):
        await ctx.send(message)


class MyBot(commands.Bot):
    def __init__(self, *args, **kwargs):
        super.__init__(*args, **kwargs)
        databaseHandler = DatabaseHandler(self)

    async def on_ready(self):
        print(f'Logged in as {myBot.user.name} (ID: {myBot.user.id})')
        print('-------')

    async def add_cog(self, cog: commands.Cog):
        super().add_cog(cog)


myBot = MyBot(("!", "$"))

myBot.add_cog(Echo())

keep_alive.keep_alive()

myBot.run(os.getenv('TOKEN'))
