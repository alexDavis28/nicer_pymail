class NicerPyMailException(Exception):
    pass


class ClientException(NicerPyMailException):
    pass


class EmailException(NicerPyMailException):
    pass


class AuthenticationException(ClientException):
    def __str__(self):
        return "Authentication failed, check that your username and password are correct, and that your account " \
               "allows less secure applications."


class AttachmentNotFoundException(EmailException):
    def __init__(self, file: str):
        self.file = file

    def __str__(self):
        return f"This file wasn't found: {self.file}"


class DuplicateAttachment(EmailException):
    def __init__(self, file: str):
        self.file = file

    def __str__(self):
        return f"Multiple copies of the same file can't be attached: {self.file}"
