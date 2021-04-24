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

class GuildNotAdded(databaseExceptions.DatabaseException):
    """ Failed to Add Guild to Database """
    def __init__(self, message="Failed to Store Guild to Database"):
        super(GuildNotAdded, self).__init__(message)

class GuildNotUpdated(databaseExceptions.DatabaseException):
    """ Failed to Update Guild in Database """
    def __init__(self, message="Failed to Update Guild in Database"):
        super(GuildNotUpdated, self).__init__(message)

class CommitToDatabaseFailed(databaseExceptions.DatabaseException):
    """ Failed to Commit to Database """
    def __init__(self, message="Failed to Commit to Database"):
        super(CommitToDatabaseFailed, self).__init__(message)

class GuildNotRemoved(databaseExceptions.DatabaseException):
    """ Failed to Remove Guild from Database """
    def __init__(self, message="Failed to Remove Guild From Database"):
        super(GuildNotRemoved, self).__init__(message)
        

class DatabaseHandler():
    def __init__(self, owner, databaseFile="./databases/database.db"):
        self.owner = owner
        self.sqlCreateGuildTable = """CREATE TABLE IF NOT EXISTS guilds (
                                            id integer PRIMARY KEY,
                                            guild_id integer NOT NULL,
                                            name text NOT NULL,
                                            owner_id integer NOT NULL,
                                            text_channel_id integer,
                                            voice_channel_id integer,
                                            role_id integer                                           
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
            raise ConnectionNotEstablished(message=e.__str__())

        logging.info("Database Connection Initialized Successfully")

        return conn


    def CreateTable(self, createTableStatement):
        logging.info("Database Table Initializing...")

        try:
            cur = self.connection.cursor()
            cur.execute(createTableStatement)
        except sqlite3.Error as e:
            raise TableNotCreated(message=e.__str__())

        logging.info("Database Table Initialized Successfully")

        return

    
    async def CommitToDatabase(self, sql, toCommit=None):
        with self.connection:
            try:
                cur = self.connection.cursor()
                if toCommit is None: cur.execute(sql)
                else: cur.execute(sql, toCommit)
                self.connection.commit()
            except:
                raise CommitToDatabaseFailed()

            return cur.lastrowid


    async def AddNewGuild(self, guildId, guildName, ownerId, textChannelId=None, voiceChannelid=None, roleId=None):
        sql = """ INSERT INTO guilds(guild_id, name, owner_id, text_channel_id, voice_channel_id, role_id)
              VALUES(?,?,?,?,?,?)"""

        try:
            guild = await self.CreateNewGuild(guildId, guildName, ownerId, textChannelId, voiceChannelid, roleId)
            lstId = await self.CommitToDatabase(sql, guild)
        except CommitToDatabaseFailed as e:
            raise GuildNotAdded(message=e.__str__())
        except:
            raise GuildNotAdded()
        
        logging.debug("Guild Added to Database")

        return lstId


    async def CreateNewGuild(self, guildId, guildName, ownerId, textChannelId=None, voiceChannelId=None, roleId=None):
        guild = (guildId, guildName, ownerId, textChannelId. voiceChannelId, roleId)

        logging.info("Create New Guild")
        logging.debug(f'New Guild Created Name: {guildName} and Id: {guildId}')
        return guild


    async def UpdateGuild(self, guildId, textChannelId=None, voiceChannelId=None, roleId=None):
        sql = """ UPDATE guilds
                    SET text_channel_id = ?,
                        voice_channel_id = ?,
                        role_id = ?
                    WHERE guild_id = ?"""

        try:
            await self.CommitToDatabase(sql, (textChannelId, voiceChannelId, roleId, guildId))
        except CommitToDatabaseFailed as e:
            raise GuildNotUpdated(message=e.__str__())
        except:
            raise GuildNotUpdated()

        logging.debug("Guild Updated in Database")

        return


    async def RemoveGuild(self, guildId):
        sql = """ DELETE FROM guilds WHERE guild_id = ? """
        try:
            await self.CommitToDatabase(sql, (guildId,))
        except CommitToDatabaseFailed as e:
            raise GuildNotRemoved(message=e.__str__())
        except:
            raise GuildNotRemoved()

        logging.debug("Guild Removed from Database")

        return

    async def RemoveAllGuilds(self):
        sql = """ DELETE FROM guilds """
        try:
            await self.CommitToDatabase(sql)
        except CommitToDatabaseFailed as e:
            raise GuildNotRemoved(message=e.__str__())
        except:
            raise GuildNotRemoved(message="Failed to Remove All Guilds From Database")

        logging.debug("All Guilds Removed from Database")
        
        return

