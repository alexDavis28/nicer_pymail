class NicerPyMailException(Exception):
    pass


class ClientException(NicerPyMailException):
    pass


class AuthenticationError(ClientException):
    def __str__(self):
        return "Authentication failed, check that your username and password are correct, and that your account " \
               "allows less secure applications."
