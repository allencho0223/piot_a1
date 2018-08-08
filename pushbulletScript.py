#!/usr/bin/env python3
import requests
import json
import os
from data_collector import getTemperature

ACCESS_TOKEN="o.KsZjOYKtrgxsQP1nc8QhkBq22vvVOai3"

def send_notification_via_pushbullet(title, body):
    """ Sending notification via pushbullet.
        Args:
            title (str) : title of text.
            body (str) : Body of text.
    """
    data_send = {"type": "note", "title": title, "body": body}
 
    resp = requests.post('https://api.pushbullet.com/v2/pushes', data=json.dumps(data_send),
                         headers={'Authorization': 'Bearer ' + ACCESS_TOKEN, 
                         'Content-Type': 'application/json'})
    if resp.status_code != 200:
        raise Exception('Something wrong')
    else:
        print('complete sending')

#main function
def main():
    temperature = getTemperature()
    if temperature < 20:
        send_notification_via_pushbullet(temperature, "Current temperature of this place is below 20 degree centigrade. Don't forget to bring a sweater :)")
    # ip_address = os.popen('hostname -I').read()
    # send_notification_via_pushbullet(ip_address, "From Raspberry Pi")

#Execute
main()
