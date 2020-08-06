class Email:
    def __init__(self, subject: str = "None", plaintext: str = "None", cc: list = [], bcc: list = [],
                 attachments: list = [],
                 from_address: str = None,
                 to_address: str = None, html: str = None):
        self.subject = subject
        self.plaintext = plaintext
        self.bcc = bcc
        self.cc = cc
        self.attachments = attachments
        self.from_address = from_address
        self.to_address = to_address
        self.html = html

    def add_attachment(self, path_to_file: str):
        self.attachments.append(path_to_file)
