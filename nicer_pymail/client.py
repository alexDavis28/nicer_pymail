import smtplib
import ssl
import imaplib
from os.path import basename
import os
from email.header import decode_header
import email as py_email
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

from .exceptions import *
from .email import Email


class Client:
    def __init__(self, email_address: str, password: str, outgoing_server: str = "smtp.gmail.com",
                 incoming_server: str = "imap.gmail.com", port: int = 465,
                 do_print: bool = False):
        self.incoming_server = incoming_server
        self.email_address = email_address
        self.password = password
        self.outgoing_server = outgoing_server
        self.port = port
        self.do_print = do_print

        context = ssl.create_default_context()

        with smtplib.SMTP_SSL(self.outgoing_server, self.port, context=context) as server:
            try:
                server.login(self.email_address, self.password)
                if do_print:
                    print("Client created")
            except smtplib.SMTPAuthenticationError:
                raise AuthenticationException

    def send_plaintext_email(self, recipient_email: str, msg: str):
        """Send a simple plaintext email to the specified address"""

        context = ssl.create_default_context()

        with smtplib.SMTP_SSL(self.outgoing_server, self.port, context=context) as server:
            try:
                server.login(self.email_address, self.password)
            except smtplib.SMTPAuthenticationError:
                raise AuthenticationException

            server.sendmail(self.email_address, recipient_email, msg)
        if self.do_print:
            print("Sent email")

    def send_email(self, recipient_email: str, email: Email, cc: list = [], bcc: list = []):
        message = MIMEMultipart("alternative")

        message["Subject"] = email.subject
        message["From"] = self.email_address
        message["To"] = recipient_email

        if cc:
            message["Cc"] = ",".join(cc)

        rcpt = cc + bcc + [recipient_email]

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
                if email.attachments.count(file) > 1:
                    raise DuplicateAttachment(file)
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

        context = ssl.create_default_context()

        with smtplib.SMTP_SSL(self.outgoing_server, self.port, context=context) as server:
            try:
                server.login(self.email_address, self.password)
            except smtplib.SMTPAuthenticationError:
                raise AuthenticationException

            server.sendmail(self.email_address, rcpt, message.as_string())
        if self.do_print:
            print("Sent email")

    def get_emails(self, inbox: str = "INBOX", limit=10):

        emails = []

        imap = imaplib.IMAP4_SSL(self.incoming_server)
        imap.login(self.email_address, self.password)

        imap.select(inbox)

        _, data = imap.search(None, "ALL")

        nums = data[0].split()[::-1]

        if len(nums) > limit:
            nums = nums[:limit]

        for num in nums:
            # print(data[0])
            _, msg_data = imap.fetch(num, "(RFC822)")
            email = Email()

            for response_part in msg_data:
                if isinstance(response_part, tuple):
                    # msg = py_email.message_from_bytes(response_part[1])
                    #
                    # subject = decode_header(msg["Subject"])[0][0]
                    # from_address = msg.get("From")

                    attachments = []

                    msg = py_email.message_from_bytes(response_part[1])
                    from_address = msg["from"]
                    subject = msg["subject"]
                    to_address = msg["to"]

                    if msg.is_multipart():
                        plaintext = ""
                        html = None
                        for part in msg.get_payload():
                            content_disposition = str(part.get("Content-Disposition"))

                            if part.get_content_type() == "text/plain" and "attachment" not in content_disposition:
                                plaintext = part.get_payload()

                            elif part.get_content_type() == "text/html" and "attachment" not in content_disposition:
                                html = part.get_payload()

                            elif "attachment" in content_disposition:
                                file = [part.get_filename(), part.get_payload(decode=True)]
                                attachments.append(file)

            email.subject = subject
            email.from_address = from_address
            email.recipients = to_address
            email.plaintext = plaintext
            email.html = html
            email.attachments = attachments
            emails.append(email)

        imap.close()

        return emails
