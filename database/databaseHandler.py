import json
import random
import asyncio
import sqlite3
from sqlite3 import Error


class DatabaseHandler():
    def __init__(self, owner, databaseFile="./databases/database.db"):
        self.owner = owner
        self.connection = self.CreateConnection(databaseFile)

    def CreateConnection(self, dbFile):
        conn = None
        try:
            conn = sqlite3.connect(dbFile)
        except Error as e:
            print(e)

        return conn

    async def AddServer(self, server):
        pass

    async def AddChannelToServer(self, server, channel):
        pass

    async def RemoveServer(self, server):
        pass

    async def ChangeChannel(self, server, channel):
        pass
