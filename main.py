# This is a project for OSU hackathon fall 2022
# Tony Young
# Clinton Merritt


import smtplib, ssl, email, requests
from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Create MIMEMultipart object
msg = MIMEMultipart("alternative")
msg["Subject"] = "multipart test"
msg["From"] = sender_email
msg["To"] = receiver_email


