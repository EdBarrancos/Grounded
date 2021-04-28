#Standard Library Input


#Third Party Inputs


#Local Application Inputs



class Wrapper():
    def BoldWrapper(self, message):
        return f'**{message}**'

    def UpperWrapper(self, message):
        return message.upper()

    def ItalicWrapper(self, message):
        return f'*{message}*'

    def AllAngryWrapper(self, message):
        return f'{self.BoldWrapper(self.ItalicWrapper(self.UpperWrapper(message+"!")))}'
    
    def CodeWrapper(self, message):
        return f'`{message}`'

    def CodeBlockWrapper(self, message):
        return f'```{message}```'

    def BackQuoteWrapper(self, message):
        return f'> {message}'