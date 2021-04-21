import json
import random

_databaseIDSize = 3


class DatabaseHandler():
    def __init__(self, owner):
        self.owner = owner
        self.database = f"database{generateRandomId(_databaseIDSize)}.json"

        print(self.database)


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
