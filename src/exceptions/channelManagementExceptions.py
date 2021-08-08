class ChannelManagementException(Exception):
    """ Base Exception Class For Errors Thrown by GrChannel """

    def __init__(self, message="Server Channel Management Error"):
        self.message = message
        super(ChannelManagementException, self).__init__(self.message)

    def __str__(self):
        return self.message
