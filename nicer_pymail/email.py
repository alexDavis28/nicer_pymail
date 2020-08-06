class Email:
    def __init__(self, subject: str = "None", plaintext: str = "None",
                 attachments: list = [],
                 from_address: str = None,
                 recipients: str = None, html: str = None):
        self.subject = subject
        self.plaintext = plaintext
        self.attachments = attachments
        self.from_address = from_address
        self.recipients = recipients
        self.html = html

    def add_attachment(self, path_to_file: str):
        self.attachments.append(path_to_file)
