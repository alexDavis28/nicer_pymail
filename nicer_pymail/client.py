import smtplib
import ssl
from os.path import basename
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

from .exceptions import *
from .email import Email


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
                raise AuthenticationException

    def send_plaintext_email(self, recipient_email: str, msg: str):
        """Send a simple plaintext email to the specified address"""
        with smtplib.SMTP_SSL(self.host, self.port, context=self.context) as server:
            try:
                server.login(self.email_address, self.password)
            except smtplib.SMTPAuthenticationError:
                raise AuthenticationException

            server.sendmail(self.email_address, recipient_email, msg)
        if self.do_print:
            print("Sent email")

    def send_email(self, recipient_email: str, email: Email):
        message = MIMEMultipart("alternative")

        message["Subject"] = email.subject
        message["From"] = self.email_address
        message["To"] = recipient_email

        text = email.plaintext

        if email.html:
            html = email.html
        else:
            html = f"""\
<html>
  <body>
    <p>{text}</p>
  </body>
</html>
"""

        plaintext_part = MIMEText(text, "plain")
        html_text_part = MIMEText(html, "html")

        message.attach(plaintext_part)
        message.attach(html_text_part)

        if email.attachments:
            for file in email.attachments:
                try:
                    with open(file, "rb") as f:
                        attachment_part = MIMEApplication(
                            f.read(),
                            Name=basename(file)
                        )
                    attachment_part['Content-Disposition'] = f'attachment; filename="{basename(file)}"'
                    message.attach(attachment_part)
                except FileNotFoundError:
                    raise AttachmentNotFoundException(file)

        with smtplib.SMTP_SSL(self.host, self.port, context=self.context) as server:
            try:
                server.login(self.email_address, self.password)
            except smtplib.SMTPAuthenticationError:
                raise AuthenticationException

            server.sendmail(self.email_address, recipient_email, message.as_string())
        if self.do_print:
            print("Sent email")
