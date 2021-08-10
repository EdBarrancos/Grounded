# Standard Library Imports

# Third Party Imports
import discord
from discord import guild
from discord.errors import Forbidden
from discord.ext import commands
import logging

# Local Application Imports
import wrapper
import exceptions.roleManagementExceptions as roleExceptions


class RoleNotDefined(roleExceptions.RoleManagementException):
    """ Server Role Not Defined """
    def __init__(self, message="Server Role Not Defined"):
        super(RoleNotDefined, self).__init__(message)


#defineR
nameDR = "defineR"
aliasesDR = ("dr", "dR", "define_role")
helpMessageDR = ('After the command type the name of the role,'
                 ' you want badbehavioured users  be attatched!')
briefMessageDR = 'Define the Role for badbehavioured users'


#getR
nameGR = "getR"
aliasesGR = ("gr", "gR", "get_role")
helpMessageGR = ("The Bot will repeat the name of the current Grounded Role")
briefMessageGR = ("Get the Grounded Role")


#createR
nameCR = "createR"
aliasesCR = ("cr", "cR", "create_role")
helpMessageCR = ('The bot will create a role if not created beforehand'
                 'and define it as the Grounded Role')
briefMessageCR = "I'll create the tag of the Miss behaved!"
roleName = "GROUNDED"


class GrRoles(commands.Cog):

    ################
    # INITIALIZERS #
    ################


    def __init__(self, handler):
        self.handler = handler
        self.wrapper = wrapper.Wrapper()
        logging.info("GrRoles Initialized")


    async def SetChannelsHandler(self, channelsHandler):
        self.channelsHandler = channelsHandler
        return


    ############
    # COMMANDS #
    ############


    @commands.command(name=nameDR, aliases=aliasesDR, help=helpMessageDR, brief=briefMessageDR)
    async def DefineRole(self, ctx,*, roleName:str):
        role = discord.utils.get(
            ctx.guild.roles, name=roleName)
        try:
            await self.SetRole(role, ctx.guild.id)
        except RoleNotDefined:
            await ctx.send(f'{self.wrapper.BackQuoteWrapper(self.wrapper.AllAngryWrapper("No such Role!"))}')
            return
        except:
            raise

        await self.GetRole(ctx)
        return


    @commands.command(name=nameGR, aliases=aliasesGR, help=helpMessageGR, brief=briefMessageGR)
    async def GetRole(self, ctx):
        try:
            roleId = await self.GetRoleId(ctx.guild)
        except:
            await ctx.send(f'{self.wrapper.BackQuoteWrapper(self.wrapper.AllAngryWrapper("I Cant Get the Role For you NOW!!"))}')
            return

        if roleId == None:
            await ctx.send(f'{self.wrapper.BackQuoteWrapper(self.wrapper.AllAngryWrapper("No Role Defined!"))}')
            return


        await ctx.send(f'This Server\'s Grounded Role is the {self.wrapper.CodeWrapper(ctx.guild.get_role(roleId).name)} role!')
        await ctx.send(f'{self.wrapper.AllAngryWrapper("Any problem With that????")}')

    
    @commands.command(name=nameCR, aliases=aliasesCR, help=helpMessageCR, brief=briefMessageCR)
    async def CreateRole(self, ctx):
        if await self.DoesRoleExistInGuild(ctx.guild, roleName):
            await ctx.send(f'{self.wrapper.BackQuoteWrapper(self.wrapper.AllAngryWrapper("GROUNDED already Created!"))}')
            await self.DefineRole(ctx, roleName=roleName)
            return

        try:
            role = await ctx.guild.create_role(name=roleName, mentionable=True, colour=discord.Colour.red(), hoist=True)
        except Forbidden:
            await ctx.send(f'{self.wrapper.BackQuoteWrapper(self.wrapper.AllAngryWrapper("I dont have permission to create a role, apperantly!"))}')
            return
        else:
            logging.info("Grounded Role Created")

        try:
            await self.SetRole(role, guildId = ctx.guild.id)
        except RoleNotDefined:
            await ctx.send(f'{self.wrapper.BackQuoteWrapper(self.wrapper.AllAngryWrapper("No such Role!"))}')
            return
        except:
            raise

        await self.GetRole(ctx)
        return


    ##########################
    # NON COMMANDS FUNCTIONS #
    ##########################


    async def DoesRoleExistInGuild(self, guild, roleName):
        if discord.utils.get(guild.roles, name=roleName) == None:
            return False
        return True

    
    async def SetRole(self, role, guildId = None):
        if role == None and guildId == None:
            raise RoleNotDefined()
        if role == None and guildId != None:
            await self.handler.owner.databaseHandler.UpdateGuild(guildId, roleId = None)
            raise RoleNotDefined()

        try:
            if role.id == await self.handler.owner.databaseHandler.GetGuildRoleId(role.guild.id):
                logging.info("Current Role same as Role to be Set")
                return
            await self.handler.owner.databaseHandler.UpdateGuild(role.guild.id, roleId=role.id)
        except:
            raise


    async def GetRoleId(self, guild): 
        roleId = await self.handler.owner.databaseHandler.GetGuildRoleId(guild.id)

        if roleId == None:
            return None

        role = discord.utils.get(guild.roles, id=roleId)
        if role == None:
            try:
                await self.SetRole(None, guild.id)
            except:
                raise
            return None

        return roleId