# Standard Library Imports
import random
import asyncio

# Third Party Imports
import sqlite3

# Local Application Imports
import exceptions.databaseExceptions as databaseExceptions


#Errors
class ConnectionNotEstablished(databaseExceptions.DatabaseException):
    """ Connection Failed to be Established """
    def __init__(self, message="Connection Failed to be Established"):
        super(ConnectionNotEstablished, self).__init__(message)
        

class DatabaseHandler():
    def __init__(self, owner, databaseFile="./databases/database.db"):
        self.owner = owner
        self.connection = self.CreateConnection(databaseFile)

    def CreateConnection(self, dbFile):
        conn = None
        try:
            conn = sqlite3.connect(dbFile)
        except sqlite3.Error as e:
            raise ConnectionNotEstablished(e.__str__())

        return conn

    async def AddServer(self, server):
        pass

    async def AddChannelToServer(self, server, channel):
        pass

    async def RemoveServer(self, server):
        pass

    async def ChangeChannel(self, server, channel):
        pass
