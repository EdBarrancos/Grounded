# Standard Library Imports
import random
import asyncio

# Third Party Imports
import sqlite3
import logging

# Local Application Imports
import exceptions.databaseExceptions as databaseExceptions


#Errors
class ConnectionNotEstablished(databaseExceptions.DatabaseException):
    """ Connection Failed to be Established """
    def __init__(self, message="Connection Failed to be Established"):
        super(ConnectionNotEstablished, self).__init__(message)

class TableNotCreated(databaseExceptions.DatabaseException):
    """ Failed to Create a Table in the Database """
    def __init__(self, message="Table Failed to be Created"):
        super(TableNotCreated, self).__init__(message)
        

class DatabaseHandler():
    def __init__(self, owner, databaseFile="./databases/database.db"):
        self.owner = owner
        self.sqlCreateGuildTable = """CREATE TABLE IF NOT EXISTS guild (
                                            id integer PRIMARY KEY,
                                            guild_id integer NOT NULL,
                                            name text NOT NULL,
                                            owner_id integer NOT NULL,
                                            text_channel_id integer,
                                            voice_channel_id integer                                            
                                        );  """


        self.connection = self.CreateConnection(databaseFile)

        #Error Checking
        
        if self.connection is None: raise ConnectionNotEstablished("Failed to establish database connection")
        self.CreateTable(self.sqlCreateGuildTable)

    def CreateConnection(self, dbFile):
        logging.info("Database Connection Initializing ...")

        conn = None
        try:
            conn = sqlite3.connect(dbFile)
        except sqlite3.Error as e:
            raise ConnectionNotEstablished(e.__str__())

        logging.info("Database Connection Initialized Successfully")

        return conn

    def CreateTable(self, createTableStatement):
        logging.info("Database Table Initializing...")

        try:
            c = self.connection.cursor()
            c.execute(createTableStatement)
        except sqlite3.Error as e:
            raise TableNotCreated(e.__str__())

        logging.info("Database Table Initialized Successfully")

        return
    
    

    async def AddServer(self, server):
        pass

    async def AddChannelToServer(self, server, channel):
        pass

    async def RemoveServer(self, server):
        pass

    async def ChangeChannel(self, server, channel):
        pass
