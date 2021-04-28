#Standard Library Imports

#Third Party Imports
import discord
from discord.ext import commands
import logging

#Local Application Imports
import wrapper

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
        self.wrapper = wrapper.Wrapper()
        logging.info("GrChannels Initialized")

    @commands.command(name=nameDV, aliases=aliasesDV, help=helpMessageDV, brief=briefMessageDV)
    async def defineV_channel(self, ctx, channel_name: str):
        channel = discord.utils.get(ctx.guild.voice_channels, name=channel_name)
        if channel == None:
            await ctx.send(f'No such Channel!')
            return
            
        await self.handler.owner.databaseHandler.UpdateGuild(ctx.guild.id, voiceChannelId=channel.id)
    

    @commands.command(name=nameGV, aliases=aliasesGV, help=helpMessageGV, brief=briefMessageGV)
    async def getV_channel(self, ctx):
        voiceChannelId = await self.handler.owner.databaseHandler.GetGuildVoiceChannelId(ctx.guild.id)
        await ctx.send(f'This Server\'s Grounded channel is the {self.wrapper.CodeWrapper(ctx.guild.get_channel(voiceChannelId).name)} channel!')
        await ctx.send(f'{self.wrapper.BoldWrapper("Any problem With that????")}')