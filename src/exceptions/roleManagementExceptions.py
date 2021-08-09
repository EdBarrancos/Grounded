class RoleManagementException(Exception):
    """ Base Exception Class For Errors Thrown by GrRoles """

    def __init__(self, message="Server Role Management Error"):
        self.message = message
        super(RoleManagementException, self).__init__(self.message)

    def __str__(self):
        return self.message
