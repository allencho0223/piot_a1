#!/usr/bin/env python3
#Acknowledgements: send_notification_via_pushbullet taken from PIoT lab 4.
#Used for academic purposes

from sense_hat import SenseHat
import requests
import json
import time
import os
from accurate_temperature import return_accuratetemp
 
def send_notification_via_pushbullet(title, body):
    
    """ Sending notification via pushbullet.
        Args:
            title (str) : title of text.
            body (str) : Body of text.
    """
    data_send = {"type": "note", "title": title, "body": body}
    # Access token for Alex
    # ACCESS_TOKEN = 'o.gmSIfrIUwZwFFGrQlLYU8tkRW116p3k3'
    # Access token for Allen    
    ACCESS_TOKEN = "o.p9NVAaowrt8njd3fbZB4fNT4wuMhvUmp"
    
    resp = requests.post('https://api.pushbullet.com/v2/pushes',
                        data = json.dumps(data_send), headers={'Authorization': 'Bearer ' 
                        + ACCESS_TOKEN, 'Content-Type': 'application/json'})
    if resp.status_code != 200:
        raise Exception('Something wrong')

def main():
    
    body_message = "You should bring a jacket."
    cold_temp=20
    
    # Retrieve current temperature
    temperature = return_accuratetemp()

    if temperature < cold_temp:
        temperature_message = ('It is {0:0.1f} degrees celsius'.format(temperature))
    elif temperature >= cold_temp:
        temperature_message = ('It is {0:0.1f} degrees celsius'.format(temperature))
        body_message = "You do not need a jacket today"
    
    # Send a notification from pushbullet api to a user assigned with appropriate access token
    send_notification_via_pushbullet(temperature_message, body_message)

main()