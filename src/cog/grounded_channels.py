#Standard Library Imports

#Third Party Imports
import discord
from discord.ext import commands
import logging

#Local Application Imports


#defineV
nameDV = "defineV"
aliasesDV = ("dV", "dv", "define_voice")
helpMessageDV = ('Define the Grounded Voice Channel,'
                'a channel that your badbehavioured users in voice will be redirected to!')
briefMessageDV = 'Define the Voice Channel for badbehavioured users'


#getV
nameGV = "getV"
aliasesGV = ("gV", "gv", "get_voice")
helpMessageGV = "Get the Grounded Voice Channel"
briefMessageGV = "Get the Grounded Voice Channel"


class GrChannels(commands.Cog):
    def __init__(self, handler):
        self.handler = handler
        logging.info("GrChannels Initialized")

    @commands.command(name=nameDV, aliases=aliasesDV, help=helpMessageDV, brief=briefMessageDV)
    async def defineV_channel(self, ctx, channel_name: str):
        channel = discord.utils.get(ctx.guild.voice_channels, name=channel_name)
        await self.handler.owner.databaseHandler.UpdateGuild(ctx.guild.id, voiceChannelId=channel.id)
    

    @commands.command(name=nameGV, aliases=aliasesGV, help=helpMessageGV, brief=briefMessageGV)
    async def getV_channel(self, ctx):
        await self.handler.owner.databaseHandler.GetGuild(ctx.guild.id)