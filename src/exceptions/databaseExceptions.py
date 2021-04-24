class DatabaseException(Exception):
    """ Base Exception Class For Errors Thrown by DatabaseHandler """
    def __init__(self, message="Database Error"):
        self.message = message
        super(DatabaseException, self).__init__(self.message)

    def __str__(self):
        return self.message