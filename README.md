# nicer_pymail
Python package to make interfacing with email systems (mostly gmail) easier


# Quickstart
This should give you a basic understanding of how to use this package

## Creating a client
```python
from nicer_pymail import Client

client = Client("example_email@gmail.com", "password")
```
The above code creates a client object that is used to log into the smtp server.
By default, the object treats the email address as a gmail one, to use a different host specify it with the keyword argument `host`.

## Sending a plaintext email
```python
from nicer_pymail import Client

client = Client("example_email@gmail.com", "password")
recipient_email = "example_email2@gmail.com"
message = "Hello There!"
client.send_plaintext_email(recipient_email, message)
```
The above code creates a client, then sends a simple email with the value of `message` as the body of the email to the specified address.
This method can't set a subject line for the email.

## Sending a plaintext email with a subject line
```python
from nicer_pymail import Client, Email

client = Client("example_email@gmail.com", "password")

message = Email(
    subject_line="Hello There!",
    message_plaintext="General Kenobi!",
)

client.send_email("example_email2@gmail.com", message)
```
The above code will send an email with the subject line `Hello There` and the text `General Kenobi` to the specified address.

## Alternative way of creating an email
```python
from nicer_pymail import Client, Email

client = Client("example_email@gmail.com", "password")

message = Email()
message.subject_line = "Hello There!"
message.message_plaintext = "General Kenobi!"

client.send_email("example_email2@gmail.com", message)
```
Any attribute of the `Email` object can be set or changed after initialisation.

## Using html for the email text
```python
from nicer_pymail import Client, Email

client = Client("example_email@gmail.com", "password")

html_text = """\
<html>
  <body>
    <p>Hi,<br>
      I am sending this email with <b>python!</b><br>
      This is cool.
    </p>
  </body>
</html>
"""

message = Email(
    subject_line="HTML email",
    message_plaintext="Hi,\nI am sending this email with python!\nThis is cool.",
    html=html_text
)

client.send_email("example_email2@gmail.com", message)
```
The above code will send an email with html formatting (as defined in the `html_text` variable) to the specified address.

## Adding attachments to the email
```python
from nicer_pymail import Client, Email

client = Client("example_email@gmail.com", "password")

file_path = "C:\\Users\\Alex\\Desktop\\file.pdf"

message = Email(
    subject_line="Hello There!",
    message_plaintext="General Kenobi!",
    attachments = [file_path]
)

# Or:

message = Email(
    subject_line="Hello There!",
    message_plaintext="General Kenobi!"
)

message.add_attachment(file_path)

client.send_email("example_email2@gmail.com", message)
```
The attachments of the email are stored as a list, so there are two ways of adding attachments. The second is preferable imo.
The first way of adding attachments defines the file paths during initialisation as part of a list. The second way calls a method of the `Email` object to just add the attachment to the internal list.
**The file path must be an absolute one.**

## Disclaimer
This package is not great, most of it was written far too late at night, and I have honestly no idea what I'm doing. This is mostly a personal project made for fun, but any suggestions are appreciated. :) 
