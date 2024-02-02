import os
import smtplib, ssl
from dotenv import load_dotenv

load_dotenv()


def send_email(message):
    host = "smtp.gmail.com"
    port = 465
    username = os.environ["email_username"]
    password = os.environ["email_password"]
    receiver = os.environ["email_receiver"]
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)

