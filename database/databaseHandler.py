import json
import random
import asyncio
import os

_databaseIDSize = 3


class DatabaseHandler():
    def __init__(self, owner):
        self.owner = owner
        self.database = f"./databases/database{generateRandomId(_databaseIDSize)}.json"

        print(self.database)

    async def createDatabaseFile(self):
        f = open(self.database, "x")
        f.close()

    async def deleteDatabase(self):
        if os.path.exists(self.database):
            os.remove(self.database)


def generateRandomId(nbrSize: int):
    if nbrSize < 1:
        raise Exception("Invalid Database Id")
    if nbrSize == 1:
        beg = 0
        end = 9
    elif nbrSize == 2:
        beg = 10
        end = 99
    else:
        beg = 10**nbrSize
        end = 10**(nbrSize+1) - 1

    return random.randrange(beg, end)
