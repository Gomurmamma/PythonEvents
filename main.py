# This is a project for OSU hackathon fall 2022
# Tony Young
# Clinton Merritt

import datetime
import os
import requests
import smtplib
import time
from email.message import EmailMessage
from email.mime.text import MIMEText

from dotenv import load_dotenv, find_dotenv
from jinja2 import Environment

import html_template

load_dotenv(find_dotenv())

# Create message base & fields for email
msg = EmailMessage()
msg["Subject"] = "Tonight's Featured Events in Your Area!"
msg["From"] = os.getenv('sender_email')
msg["To"] = os.getenv('receiver_email')

# environment variables
sender_email = os.getenv('sender_email')
receiver_email = os.getenv('receiver_email')
client_id = os.getenv('client_id')
client_secret = os.getenv('client_secret')
password = os.getenv('password')

# SeatGeek Query params
# Lat & Lng: Bk,Ny
# Event type: Concert
# Radius: 30 mi (default)
# Per page: 10 (default)
# page: 1 (default)
response = requests.get(
    f'https://api.seatgeek.com/2/events?lat=40.650002&lon=-73.949997&client_id={client_id}&type=concert'
    f'&&client_secret={client_secret}')

events = response.json()['events']

# List for formatted events
events_list = []

# Extract relevant event data and append to list
for event in events:
    title = event['title']
    ticket_url = event['url']
    date = event['datetime_local']

    date_time_obj = datetime.datetime.strptime(date, '%Y-%m-%dT%H:%M:%S')
    event_month = date_time_obj.strftime('%B')
    event_day = date_time_obj.day

    venue = event['venue']
    venue_name = venue['name_v2']
    city = venue['city']
    state = venue['state']

    performers = event['performers']
    performer = performers[0]
    image_url = performer['image']

    formatted_event = {'formatted_title': title, 'formatted_ticket_url': ticket_url, 'formatted_month': event_month,
                       'formatted_day': str(event_day), 'formatted_venue_name': venue_name, 'formatted_city': city,
                       'formatted_state': state, 'formatted_image_url': image_url,
                       }

    events_list.append(formatted_event)

# Create html message from the template and then the values from each event
events_html = MIMEText(
    Environment().from_string(html_template.template).render(
        title0=events_list[0]['formatted_title'],
        ticket_url0=events_list[0]['formatted_ticket_url'],
        month0=events_list[0]['formatted_month'],
        day0=events_list[0]['formatted_day'],
        venue0=events_list[0]['formatted_venue_name'],
        city0=events_list[0]['formatted_city'],
        state0=events_list[0]['formatted_state'],
        image_url0=events_list[0]['formatted_image_url'],
        title1=events_list[1]['formatted_title'],
        ticket_url1=events_list[1]['formatted_ticket_url'],
        month1=events_list[1]['formatted_month'],
        day1=events_list[1]['formatted_day'],
        venue1=events_list[1]['formatted_venue_name'],
        city1=events_list[1]['formatted_city'],
        state1=events_list[1]['formatted_state'],
        image_url1=events_list[1]['formatted_image_url'],
        title2=events_list[2]['formatted_title'],
        ticket_url2=events_list[2]['formatted_ticket_url'],
        month2=events_list[2]['formatted_month'],
        day2=events_list[2]['formatted_day'],
        venue2=events_list[2]['formatted_venue_name'],
        city2=events_list[2]['formatted_city'],
        state2=events_list[2]['formatted_state'],
        image_url2=events_list[2]['formatted_image_url'],
        title3=events_list[3]['formatted_title'],
        ticket_url3=events_list[3]['formatted_ticket_url'],
        month3=events_list[3]['formatted_month'],
        day3=events_list[3]['formatted_day'],
        venue3=events_list[3]['formatted_venue_name'],
        city3=events_list[3]['formatted_city'],
        state3=events_list[3]['formatted_state'],
        image_url3=events_list[3]['formatted_image_url'],
        title4=events_list[4]['formatted_title'],
        ticket_url4=events_list[4]['formatted_ticket_url'],
        month4=events_list[4]['formatted_month'],
        day4=events_list[4]['formatted_day'],
        venue4=events_list[4]['formatted_venue_name'],
        city4=events_list[4]['formatted_city'],
        state4=events_list[4]['formatted_state'],
        image_url4=events_list[4]['formatted_image_url'],
        title5=events_list[5]['formatted_title'],
        ticket_url5=events_list[5]['formatted_ticket_url'],
        month5=events_list[5]['formatted_month'],
        day5=events_list[5]['formatted_day'],
        venue5=events_list[5]['formatted_venue_name'],
        city5=events_list[5]['formatted_city'],
        state5=events_list[5]['formatted_state'],
        image_url5=events_list[5]['formatted_image_url'],
        title6=events_list[6]['formatted_title'],
        ticket_url6=events_list[6]['formatted_ticket_url'],
        month6=events_list[6]['formatted_month'],
        day6=events_list[6]['formatted_day'],
        venue6=events_list[6]['formatted_venue_name'],
        city6=events_list[6]['formatted_city'],
        state6=events_list[6]['formatted_state'],
        image_url6=events_list[6]['formatted_image_url'],
        title7=events_list[7]['formatted_title'],
        ticket_url7=events_list[7]['formatted_ticket_url'],
        month7=events_list[7]['formatted_month'],
        day7=events_list[7]['formatted_day'],
        venue7=events_list[7]['formatted_venue_name'],
        city7=events_list[7]['formatted_city'],
        state7=events_list[7]['formatted_state'],
        image_url7=events_list[7]['formatted_image_url'],
        title8=events_list[8]['formatted_title'],
        ticket_url8=events_list[8]['formatted_ticket_url'],
        month8=events_list[8]['formatted_month'],
        day8=events_list[8]['formatted_day'],
        venue8=events_list[8]['formatted_venue_name'],
        city8=events_list[8]['formatted_city'],
        state8=events_list[8]['formatted_state'],
        image_url8=events_list[8]['formatted_image_url'],
        title9=events_list[9]['formatted_title'],
        ticket_url9=events_list[9]['formatted_ticket_url'],
        month9=events_list[9]['formatted_month'],
        day9=events_list[9]['formatted_day'],
        venue9=events_list[9]['formatted_venue_name'],
        city9=events_list[9]['formatted_city'],
        state9=events_list[9]['formatted_state'],
        image_url9=events_list[9]['formatted_image_url'],
    ), "html"
)

msg.set_content(events_html, subtype="html")

# Create secure SMTP connection
start = time.time()
try:
    smtp_ssl = smtplib.SMTP_SSL(host="smtp.gmail.com")
except Exception as e:
    print("ErrorType : {}, Error : {}".format(type(e).__name__, e))
    smtp_ssl = None

print("Connection Object : {}".format(smtp_ssl))
print("Total Time Taken  : {:,.2f} Seconds".format(time.time() - start))

# Log in to email account
print("\nLogging In.....")
resp_code, response = smtp_ssl.login(sender_email, password)

print("Response Code : {}".format(resp_code))
print("Response      : {}".format(response.decode()))

# Send email
print("\nSending Mail..........")

msg.set_content(events_html, subtype="html")

response = smtp_ssl.sendmail(sender_email, receiver_email, msg.as_string())

print("List of Failed Recipients : {}".format(response))

# Log out
print("\nLogging Out....")
resp_code, response = smtp_ssl.quit()

print("Response Code : {}".format(resp_code))
print("Response      : {}".format(response.decode()))





