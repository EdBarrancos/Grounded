# Standard Library Imports

# Third Party Imports
import discord
from discord import guild
from discord.channel import VoiceChannel
from discord.errors import Forbidden
from discord.ext import commands
import logging

from discord.role import Role

# Local Application Imports
import wrapper
import exceptions.channelManagementExceptions as channelExceptions


##############
# EXCEPTIONS #
##############


class ChannelNotDefined(channelExceptions.ChannelManagementException):
    """ Server Channel Not Defined """
    def __init__(self, message="Server Channel Not Defined"):
        super(ChannelNotDefined, self).__init__(message)

class RoleNotDefined(channelExceptions.ChannelManagementException):
    """ Server Role Not Defined """
    def __init__(self, message="Server Role Not Defined"):
        super(RoleNotDefined, self).__init__(message=message)



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

# createT
nameCT = "createT"
aliasesCT = ("cT", "ct", "create_text")
helpMessageCT = ('The bot will create a voice channel if not created beforehand'
                 'and define it as the Grounded Voice Channel')
briefMessageCT = "I'll create the playground of the Miss behaved!"
channelNameT = "grounded"


class GrChannels(commands.Cog):


    ##############
    #INITIALIZERS#
    ##############


    def __init__(self, handler):
        self.handler = handler
        self.wrapper = wrapper.Wrapper()
        logging.info("GrChannels Initialized")

    
    async def SetRolesHandler(self, rolesHandler):
        self.rolesHandler = rolesHandler
        return


    ############
    # COMMANDS #
    ############


    @commands.command(name=nameDV, aliases=aliasesDV, help=helpMessageDV, brief=briefMessageDV)
    async def DefineV_channel(self, ctx, channel_name: str):
        channel = discord.utils.get(
            ctx.guild.voice_channels, name=channel_name)
        try:
            await self.SetVoiceChannel(channel)
        except ChannelNotDefined:
            await ctx.send(f'{self.wrapper.BackQuoteWrapper(self.wrapper.AllAngryWrapper("No such Channel!"))}')
            return
        except:
            raise

        try:
            await self.UpdateVoiceChannelPermissions(ctx.guild)
        except:
            await ctx.send(f'{self.wrapper.BackQuoteWrapper(self.wrapper.AllAngryWrapper("Channels permissions NOT updated!"))}')
        else:
            await ctx.send(f'{self.wrapper.BackQuoteWrapper(self.wrapper.AllAngryWrapper("Channels permissions  updated!"))}')

        await self.GetV_channel(ctx)
        return

        

    @commands.command(name=nameDT, aliases=aliasesDT, help=helpMessageDT, brief=briefMessageDT)
    async def DefineT_channel(self, ctx, channel_name: str):
        channel = discord.utils.get(
            ctx.guild.text_channels, name=channel_name)
        try:
            await self.SetTextChannel(channel)
        except ChannelNotDefined:
            await ctx.send(f'{self.wrapper.BackQuoteWrapper(self.wrapper.AllAngryWrapper("No such Channel!"))}')
            return
        except:
            raise

        try:
            await self.UpdateTextChannelPermissions(ctx.guild)
        except:
            await ctx.send(f'{self.wrapper.BackQuoteWrapper(self.wrapper.AllAngryWrapper("Channels permissions NOT updated!"))}')
        else:
            await ctx.send(f'{self.wrapper.BackQuoteWrapper(self.wrapper.AllAngryWrapper("Channels permissions  updated!"))}')

        await self.GetT_channel(ctx)
        return


    @commands.command(name=nameGV, aliases=aliasesGV, help=helpMessageGV, brief=briefMessageGV)
    async def GetV_channel(self, ctx):
        try:
            voiceChannelId = await self.GetVoiceChannelId(ctx.guild)
        except:
            await ctx.send(f'{self.wrapper.BackQuoteWrapper(self.wrapper.AllAngryWrapper("I Cant Get the Channel For you NOW!!"))}')
            return
            
        if voiceChannelId == None:
            await ctx.send(f'{self.wrapper.BackQuoteWrapper(self.wrapper.AllAngryWrapper("No Channel Defined!"))}')
            return
        
        await ctx.send(f'This Server\'s Grounded Voice channel is the {self.wrapper.CodeWrapper(ctx.guild.get_channel(voiceChannelId).name)} channel!')
        await ctx.send(f'{self.wrapper.AllAngryWrapper("Any problem With that????")}')
        return


    @commands.command(name=nameGT, aliases=aliasesGT, help=helpMessageGT, brief=briefMessageGT)
    async def GetT_channel(self, ctx):
        try:
            textChannelId = await self.GetTextChannelId(ctx.guild)
        except:
            await ctx.send(f'{self.wrapper.BackQuoteWrapper(self.wrapper.AllAngryWrapper("I Cant Get the Channel For you NOW!!"))}')
            return
            
        if textChannelId == None:
            await ctx.send(f'{self.wrapper.BackQuoteWrapper(self.wrapper.AllAngryWrapper("No Channel Defined!"))}')
            return
        
        await ctx.send(f'This Server\'s Grounded Text channel is the {self.wrapper.CodeWrapper(ctx.guild.get_channel(textChannelId).name)} channel!')
        await ctx.send(f'{self.wrapper.AllAngryWrapper("Any problem With that????")}')
        return


    @commands.command(name=nameCV, aliases=aliasesCV, help=helpMessageCV, brief=briefMessageCV)
    async def CreateV_channel(self, ctx):
        if await self.DoesChannelExistsInGuild(ctx.guild, channelNameV):
            await ctx.send(f'{self.wrapper.BackQuoteWrapper(self.wrapper.AllAngryWrapper("Grounded already Created!"))}')
            await self.DefineV_channel(ctx, channelNameV)
            return

        try:
            overwrites = await self.GetOverwritesVoiceChannel(ctx.guild)
        except RoleNotDefined:
            overwrites = None
            await ctx.send(f'{self.wrapper.BackQuoteWrapper(self.wrapper.AllAngryWrapper("Grounded Role To be defined!"))}')
        
        try:
            channel = await ctx.guild.create_voice_channel(channelNameV, overwrites=overwrites)
        except Forbidden:
            await ctx.send(f'{self.wrapper.BackQuoteWrapper(self.wrapper.AllAngryWrapper("I dont have permission to create a channel, apperantly!"))}')
            return
        else:
            logging.info("Voice Channel Created")

        try:
            await self.SetVoiceChannel(channel, guildId = ctx.guild.id)
        except ChannelNotDefined:
            await ctx.send(f'{self.wrapper.BackQuoteWrapper(self.wrapper.AllAngryWrapper("No such Channel!"))}')
            return
        except:
            raise

        await self.GetV_channel(ctx)
        return


    @commands.command(name=nameCT, aliases=aliasesCT, help=helpMessageCT, brief=briefMessageCT)
    async def CreateT_channel(self, ctx):
        if await self.DoesChannelExistsInGuild(ctx.guild, channelNameT):
            await ctx.send(f'{self.wrapper.BackQuoteWrapper(self.wrapper.AllAngryWrapper("Grounded already Created!"))}')
            await self.DefineT_channel(ctx, channelNameT)
            return

        try:
            overwrites = await self.GetOverwritesTextChannel(ctx.guild)
        except RoleNotDefined:
            overwrites = None
            await ctx.send(f'{self.wrapper.BackQuoteWrapper(self.wrapper.AllAngryWrapper("Grounded Role To be defined!"))}')

        try:
            channel = await ctx.guild.create_text_channel(channelNameT, overwrites=overwrites)
        except Forbidden:
            await ctx.send(f'{self.wrapper.BackQuoteWrapper(self.wrapper.AllAngryWrapper("I dont have permission to create a channel, apperantly!"))}')
            return             
        else:
            logging.info("Text Channel Created")

        try:
            await self.SetTextChannel(channel, guildId = ctx.guild.id)
        except ChannelNotDefined as e:
            await ctx.send(f'{self.wrapper.BackQuoteWrapper(self.wrapper.AllAngryWrapper("No such Channel!"))}')
            return
        except Exception as e:
            raise e

        await self.GetT_channel(ctx)
        return


    ######################
    #NON COMMAND FUNCTION#
    ######################


    async def GetRoleFromRolesHandler(self, guild):
        groundedRoleId = await self.rolesHandler.GetRoleId(guild)

        if groundedRoleId == None:
            raise RoleNotDefined()

        role = guild.get_role(groundedRoleId)
        
        if role == None:
            raise RoleNotDefined()
        return role

    
    async def UpdateChannelPermissions(self, ctx):
        try:
            await self.UpdateTextChannelPermissions(ctx.guild)
        except:
            await ctx.send(f'{self.wrapper.BackQuoteWrapper(self.wrapper.AllAngryWrapper("Text Channels permissions NOT updated!"))}')
        else:
            await ctx.send(f'{self.wrapper.BackQuoteWrapper(self.wrapper.AllAngryWrapper("Text Channels permissions  updated!"))}')
        

        try:
            await self.UpdateVoiceChannelPermissions(ctx.guild)
        except:
            await ctx.send(f'{self.wrapper.BackQuoteWrapper(self.wrapper.AllAngryWrapper("Voice Channels permissions NOT updated!"))}')
        else:
            await ctx.send(f'{self.wrapper.BackQuoteWrapper(self.wrapper.AllAngryWrapper("Voice Channels permissions  updated!"))}')

    
    async def UpdateTextChannelPermissions(self, guild):
        try:
            overwrites = await self.GetOverwritesTextChannel(guild)
        except RoleNotDefined:
            raise

        channel = guild.get_channel(await self.GetTextChannelId(guild))
        for key in overwrites:
            try:
                await channel.set_permissions(key, overwrite=overwrites[key])
            except:
                raise
        return

    
    async def UpdateVoiceChannelPermissions(self, guild):
        try:
            overwrites = await self.GetOverwritesVoiceChannel(guild)
        except RoleNotDefined:
            raise

        channel = guild.get_channel(await self.GetTextChannelId(guild))
        for key in overwrites:
            try:
                await channel.set_permissions(key, overwrites=overwrites[key])
            except:
                raise
        return


    async def GetOverwritesVoiceChannel(self, guild):
        try:
            role = await self.GetRoleFromRolesHandler(guild)
        except:
            raise

        overwrites={
            guild.me: discord.PermissionOverwrite(view_channel= True, connect=True),
            guild.default_role: discord.PermissionOverwrite(view_channel=True, connect=False),
            role: discord.PermissionOverwrite(view_channel=True, connect=True)
        }
        
        return overwrites


    async def GetOverwritesTextChannel(self, guild):
        try:
            role = await self.GetRoleFromRolesHandler(guild)
        except:
            raise

        overwrites={
            guild.me: discord.PermissionOverwrite(read_messages= True, send_messages=True),
            guild.default_role: discord.PermissionOverwrite(read_messages=False, send_messages=False),
            role: discord.PermissionOverwrite(read_messages=True, send_messages=True)
        }
        
        return overwrites


    async def DoesChannelExistsInGuild(self, guild, channelName):
        if discord.utils.get(guild.channels, name=channelName) == None:
            return False
        return True


    async def GetVoiceChannelId(self, guild):
        voiceChannelId = await self.handler.owner.databaseHandler.GetGuildVoiceChannelId(guild.id)

        if voiceChannelId == None:
            return None

        channel = discord.utils.get(guild.voice_channels, id=voiceChannelId)
        if channel == None:
            try:
                await self.SetVoiceChannel(None, guild.id)
            except:
                raise
            return None

        return voiceChannelId


    async def GetTextChannelId(self, guild):
        textChannelId = await self.handler.owner.databaseHandler.GetGuildTextChannelId(guild.id)

        if textChannelId == None:
            return None

        channel = discord.utils.get(guild.text_channels, id=textChannelId)
        if channel == None:
            try:
                await self.SetTextChannel(None, guild.id)
            except:
                raise
            return None

        return textChannelId


    async def SetVoiceChannel(self, channel, guildId = None):
        if channel == None and guildId == None:
            raise ChannelNotDefined()
        if channel == None and guildId != None:
            await self.handler.owner.databaseHandler.UpdateGuild(guildId, voiceChannelId = None)
            return

        try:
            if channel.id == await self.handler.owner.databaseHandler.GetGuildVoiceChannelId(channel.guild.id):
                logging.info("Current Channel same as Channel to be Set")
                return
            await self.handler.owner.databaseHandler.UpdateGuild(channel.guild.id, voiceChannelId=channel.id)
        except Exception as e:
            raise e

    
    async def SetTextChannel(self, channel, guildId = None):
        if channel == None and guildId == None:
            raise ChannelNotDefined()
        if channel == None and guildId != None:
            await self.handler.owner.databaseHandler.UpdateGuild(guildId, textChannelId = None)
            return
        try:
            if channel.id == await self.handler.owner.databaseHandler.GetGuildTextChannelId(channel.guild.id):
                logging.info("Current Channel same as Channel to be Set")
                return
            await self.handler.owner.databaseHandler.UpdateGuild(channel.guild.id, textChannelId=channel.id)
        except:
            raise