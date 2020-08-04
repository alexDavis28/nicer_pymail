import smtplib
import ssl

from .exceptions import *


class Client:
    def __init__(self, email_address: str, password: str, host: str = "smtp.gmail.com", port: int = 465,
                 do_print: bool = False):
        self.email_address = email_address
        self.password = password
        self.host = host
        self.port = port
        self.context = ssl.create_default_context()
        self.do_print = do_print

        with smtplib.SMTP_SSL(self.host, self.port, context=self.context) as server:
            try:
                server.login(self.email_address, self.password)
                if do_print:
                    print("Client created")
            except smtplib.SMTPAuthenticationError:
                raise AuthenticationError

    def send_plaintext_email(self, recipient_email: str, msg: str):
        """Send a simple plaintext email to the specified address"""
        sender_email = self.email_address
        with smtplib.SMTP_SSL(self.host, self.port, context=self.context) as server:
            try:
                server.login(self.email_address, self.password)
            except smtplib.SMTPAuthenticationError:
                raise AuthenticationError

            server.sendmail(sender_email, recipient_email, msg)
        if self.do_print:
            print("Sent email")
