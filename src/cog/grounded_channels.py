# Standard Library Imports

# Third Party Imports
import discord
from discord.ext import commands
import logging

# Local Application Imports
import wrapper

# defineV
nameDV = "defineV"
aliasesDV = ("dV", "dv", "define_voice")
helpMessageDV = ('After the command type the name of the voice channel,'
                 ' your badbehavioured users  will be redirected to in the Future!')
briefMessageDV = 'Define the Voice Channel for badbehavioured users'

# defineT
nameDT = "defineT"
aliasesDT = ("dT", "dt", "define_text")
helpMessageDT = ('After the command type the name of the text channel,'
                 ' your badbehavioured users  will be redirected to in the Future!')
briefMessageDT = 'Define the Text Channel for badbehavioured users'

# getV
nameGV = "getV"
aliasesGV = ("gV", "gv", "get_voice")
helpMessageGV = "The Bot will repeat the name of the current grounded voice channel"
briefMessageGV = "Get the Grounded Voice Channel"

# getT
nameGT = "getT"
aliasesGT = ("gT", "gt", "get_text")
helpMessageGT = "The Bot will repeat the name of the current grounded text channel"
briefMessageGT = "Get the Grounded Text Channel"

# createV
nameCV = "createV"
aliasesCV = ("cV", "cv", "create_voice")
helpMessageCV = ('The bot will create a voice channel if not created beforehand'
                 'and define it as the Grounded Voice Channel')
briefMessageCV = "I'll create the playground of the Miss behaved!"
channelNameV = "Grounded"


class GrChannels(commands.Cog):
    def __init__(self, handler):
        self.handler = handler
        self.wrapper = wrapper.Wrapper()
        logging.info("GrChannels Initialized")

    @commands.command(name=nameDV, aliases=aliasesDV, help=helpMessageDV, brief=briefMessageDV)
    async def defineV_channel(self, ctx, channel_name: str):
        channel = discord.utils.get(
            ctx.guild.voice_channels, name=channel_name)
        if channel == None:
            await ctx.send(f'{self.wrapper.BackQuoteWrapper(self.wrapper.AllAngryWrapper("No such Channel!"))}')
            return

        await self.handler.owner.databaseHandler.UpdateGuild(ctx.guild.id, voiceChannelId=channel.id)

    @commands.command(name=nameDT, aliases=aliasesDT, help=helpMessageDT, brief=briefMessageDT)
    async def defineT_channel(self, ctx, channel_name: str):
        channel = discord.utils.get(
            ctx.guild.text_channels, name=channel_name)
        if channel == None:
            await ctx.send(f'{self.wrapper.BackQuoteWrapper(self.wrapper.AllAngryWrapper("No such Channel!"))}')
            return

        await self.handler.owner.databaseHandler.UpdateGuild(ctx.guild.id, textChannelId=channel.id)

    @commands.command(name=nameGV, aliases=aliasesGV, help=helpMessageGV, brief=briefMessageGV)
    async def getV_channel(self, ctx):
        voiceChannelId = await self.handler.owner.databaseHandler.GetGuildVoiceChannelId(ctx.guild.id)

        if voiceChannelId == None:
            await ctx.send(f'{self.wrapper.BackQuoteWrapper(self.wrapper.AllAngryWrapper("No Channel Defined!"))}')
            return

        await ctx.send(f'This Server\'s Grounded Voice channel is the {self.wrapper.CodeWrapper(ctx.guild.get_channel(voiceChannelId).name)} channel!')
        await ctx.send(f'{self.wrapper.AllAngryWrapper("Any problem With that????")}')

    @commands.command(name=nameGT, aliases=aliasesGT, help=helpMessageGT, brief=briefMessageGT)
    async def getT_channel(self, ctx):
        textChannelId = await self.handler.owner.databaseHandler.GetGuildTextChannelId(ctx.guild.id)

        if textChannelId == None:
            await ctx.send(f'{self.wrapper.BackQuoteWrapper(self.wrapper.AllAngryWrapper("No Channel Defined!"))}')
            return

        await ctx.send(f'This Server\'s Grounded Text channel is the {self.wrapper.CodeWrapper(ctx.guild.get_channel(textChannelId).name)} channel!')
        await ctx.send(f'{self.wrapper.AllAngryWrapper("Any problem With that????")}')

    @commands.command(name=nameCV, aliases=aliasesCV, help=helpMessageCV, brief=briefMessageCV)
    async def createV_channel(self, ctx):
        # Check if it exists
        channel = discord.utils.get(
            ctx.guild.voice_channels, name=channelNameV)
        if channel != None:
            await ctx.send(f'{self.wrapper.BackQuoteWrapper(self.wrapper.AllAngryWrapper("Grounded already Created!"))}')
            await self.handler.owner.databaseHandler.UpdateGuild(ctx.guild.id, voiceChannelId=channel.id)
            return

        channel = await ctx.guild.create_voice_channel(channelNameV)
        await self.handler.owner.databaseHandler.UpdateGuild(ctx.guild.id, voiceChannelId=channel.id)
