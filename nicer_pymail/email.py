class Email:
    def __init__(self, subject_line: str = "None", message_plaintext: str = "None", attachments: list = [],
                 from_address: str = None,
                 to_address: str = None, html: str = None):
        self.subject = subject_line
        self.plaintext = message_plaintext
        self.attachments = attachments
        self.from_address = from_address
        self.to_address = to_address
        self.html = html

    def add_attachment(self, path_to_file: str):
        self.attachments.append(path_to_file)
