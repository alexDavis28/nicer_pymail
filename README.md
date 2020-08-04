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
By default, the object treats the email address as a gmail one, to use a different host specify it with the argument `host`

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
