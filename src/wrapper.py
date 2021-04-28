#Standard Library Input


#Third Party Inputs


#Local Application Inputs



class Wrapper():
    async def BoldWrapper(self, message):
        return f'**{message}**'

    async def UpperWrapper(self, message):
        return message.upper()

    async def ItalicWrapper(self, message):
        return f'*{message}*'