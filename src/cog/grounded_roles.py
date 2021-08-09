# Standard Library Imports

# Third Party Imports
import discord
from discord import guild
from discord.ext import commands
import logging

# Local Application Imports
import wrapper
import exceptions.roleManagementExceptions as roleExceptions



class GrRoles(commands.Cog):
    def __init__(self, handler):
        self.handler = handler
        self.wrapper = wrapper.Wrapper()
        logging.info("GrRoles Initialized")

    async def setChannelsHandler(self, channelsHandler):
        self.channelsHandler = channelsHandler
        return