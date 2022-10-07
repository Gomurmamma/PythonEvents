# This is a project for OSU hackathon fall 2022
# Tony Young
# Clinton Merritt


import smtplib, ssl, email, requests, os, datetime, jinja2
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

# other environment variables
client_id = os.getenv('client_id')
client_secret = os.getenv('client_secret')
password = os.getenv('password')

# SeatGeek Query params
# Lat & Lng: Bk,Ny
# Event type: Concert
# Radius: 30 mi (default)
# Per page: 10 (default)
# page: 1 (default)
response = requests.get(f"https://api.seatgeek.com/2/events?lat=40.650002&lon=-73.949997&client_id={client_id}&type=concert&&client_secret={client_secret}")

events = response.json()['events']

for event in events:

    for info in event:

        title = event['title']
        ticket_url = event['url']

        date = event['datetime_local']

        date_time_obj = datetime.datetime.strptime(date, '%Y-%m-%dT%H:%M:%S')
        event_month = date_time_obj.strftime('%B')
        event_day = date_time_obj.day

        venue = event['venue']

        venue_name = venue['name']
        city = venue['city']
        state = venue['state']

        performers = event['performers']

        for performer in performers:

            image_url = performer['image']

            print(title)
            print(ticket_url)
            print(event_month, event_day)
            print(venue_name)
            print(city)
            print(state)
            print(image_url)



