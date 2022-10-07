# This is a project for OSU hackathon fall 2022
# Tony Young
# Clinton Merritt


import smtplib, ssl, email, requests, os
from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

# Create MIMEMultipart object
msg = MIMEMultipart("alternative")
msg["Subject"] = "multipart test"
msg["From"] = os.getenv('sender_email')
msg["To"] = os.getenv('receiver_email')

# other enviornment variables
client_id = os.getenv('client_id')
client_secret = os.getenv('client_secret')
password = os.getenv('password')

print(password)
