# Standard Library Imports

# Third Party Imports
import discord
from discord import guild
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


class GrRoles(commands.Cog):
    def __init__(self, handler):
        self.handler = handler
        self.wrapper = wrapper.Wrapper()
        logging.info("GrRoles Initialized")


    async def setChannelsHandler(self, channelsHandler):
        self.channelsHandler = channelsHandler
        return

    @commands.command(name=nameDR, aliases=aliasesDR, help=helpMessageDR, brief=briefMessageDR)
    async def defineRole(self, ctx,*, roleName:str):
        role = discord.utils.get(
            ctx.guild.roles, name=roleName)
        try:
            await self.setRole(role, ctx.guild.id)
        except RoleNotDefined:
            await ctx.send(f'{self.wrapper.BackQuoteWrapper(self.wrapper.AllAngryWrapper("No such Role!"))}')
            return
        except:
            raise


    @commands.command(name=nameGR, aliases=aliasesGR, help=helpMessageGR, brief=briefMessageGR)
    async def getRole(self, ctx):
        roleId = await self.handler.owner.databaseHandler.GetGuildRoleId(ctx.guild.id)

        if roleId == None:
            await ctx.send(f'{self.wrapper.BackQuoteWrapper(self.wrapper.AllAngryWrapper("No Role Defined!"))}')
            return

        role = discord.utils.get(ctx.guild.roles, id=roleId)
        if role == None:
            try:
                await self.setRole(None, ctx.guild.id)
            except RoleNotDefined:
                await ctx.send(f'{self.wrapper.BackQuoteWrapper(self.wrapper.AllAngryWrapper("No Role Defined!"))}')
            return


        await ctx.send(f'This Server\'s Grounded Role is the {self.wrapper.CodeWrapper(role.name)} role!')
        await ctx.send(f'{self.wrapper.AllAngryWrapper("Any problem With that????")}')

    
    async def setRole(self, role, guildId = None):
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