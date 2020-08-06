# nicer_pymail
Python package to make interfacing with email systems (mostly gmail) easier

# Setup
This package is still being worked on, and isn't on pypi, so this section will explain how to install the package if you want to test it.

## Making a virtualenv
As the package is still in development, I would highly recommend installing it in a virtual environment. If you don't already know who to do that, [this tutorial is an excellent guide for how to set one up.](https://docs.python-guide.org/dev/virtualenvs/#lower-level-virtualenv)

## Installing the package
With the virtual environment active (assuming you have made one), run the following command:
```
pip install git+https://github.com/justsomeonenamedalex/nicer_pymail
```
Confirm the package is installed with:
```
pip show nicer_pymail
```

## Creating a gmail account
To use this code you will need a gmail account that allows access from less secure apps. You could do this on your personal account, however that is an **extremely bad idea** as it would make your personal account vulnerable

First [create a google account.](https://accounts.google.com/Signup).

Then, [follow this link.](https://myaccount.google.com/lesssecureapps) and turn on `Allow less secure apps`. You will receive some security alert emails, but that's why you made a new account.

Note down the email address and password.

## Running the code
If you have installed the package in a virtual environment, the code will only run when the virtual environment is active. To run the code, using a terminal, navigate to the directory where the code is, if you are using a virtual environment confirm that it is activated, then run:
```
python {filename}.py
```
In the above, replace `{filename}` with the name of whatever file you are running. You may have to replace `python` with `python3` or `python3.8` etc, depending on your installation
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
    subject="Hello There!",
    plaintext="General Kenobi!",
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
    subject="HTML email",
    plaintext="Hi,\nI am sending this email with python!\nThis is cool.",
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
    subject="Hello There!",
    plaintext="General Kenobi!",
    attachments = [file_path]
)

# Or:

message = Email(
    subject="Hello There!",
    plaintext="General Kenobi!"
)

message.add_attachment(file_path)

client.send_email("example_email2@gmail.com", message)
```
The attachments of the email are stored as a list, so there are two ways of adding attachments. The second is preferable imo.
The first way of adding attachments defines the file paths during initialisation as part of a list. The second way calls a method of the `Email` object to just add the attachment to the internal list.
**The file path must be an absolute one.**

## Using CC and BCC
```python
from nicer_pymail import Client, Email

client = Client("example_email@gmail.com", "password")

message = Email(
    subject="Hello There!",
    plaintext="General Kenobi!",
)

to_address = "example2@gmail.com"
cc_addresses = ["example3@gmail.com", "example4@example.com"]
bcc_addresses = ["example5@example.com"]

client.send_email("example_email2@gmail.com", message, cc=cc_addresses, bcc=bcc_addresses)
```
The above code will send the email to `example2@gmail.com` as well as `example3@gmail.com` and `example4@example.com`. `example5@example.com` will be bcc'ed the email.
## Disclaimer
This package is not great, most of it was written far too late at night, and I have honestly no idea what I'm doing. This is mostly a personal project made for fun, but any suggestions are appreciated. :) 
