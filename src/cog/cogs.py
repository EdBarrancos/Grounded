# Standard Library Imports

# Third Party Imports
from cog.grounded_roles import GrRoles
import discord
from discord.ext import commands

# Local Application Imports
from .echo import Echo
from .grounded_channels import GrChannels
from .grounded_roles import GrRoles


class CogHandler():
    def __init__(self, owner):
        self.owner = owner

    async def addCogs(self):
        self.owner.add_cog(Echo(self))
        grChannelCog = GrChannels(self)
        grRolesCog = GrRoles(self)
        self.owner.add_cog(grChannelCog)
        self.owner.add_cog(grRolesCog)

        await grChannelCog.setRolesHandler(grRolesCog)
        await grRolesCog.setChannelsHandler(grChannelCog)

