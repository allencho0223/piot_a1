from sense_hat import SenseHat
import requests
import json
import time
import os
import accurate_temperature
 
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
    ACCESS_TOKEN="o.KsZjOYKtrgxsQP1nc8QhkBq22vvVOai3"
    resp = requests.post('https://api.pushbullet.com/v2/pushes',
                        data = json.dumps(data_send), headers={'Authorization': 'Bearer ' 
                        + ACCESS_TOKEN, 'Content-Type': 'application/json'})
    if resp.status_code != 200:
        raise Exception('Something wrong')
    else:
        print('complete sending')

def main():
    
    head_message = "You should bring a jacket."
    sleep_time = 300  #Change to 300 (5 minutes)
    temperature_message = "It is less than 20 degrees"

    cold_temp=20
    run = 0
    while run < 1:
        t1 = accurate_temperature.sense.get_temperature_from_humidity()
        t2 = accurate_temperature.sense.get_temperature_from_pressure()
        t_cpu = accurate_temperature.get_cpu_temp()
        t = (t1 + t2) / 2
        t_corr = t - ((t_cpu - t) / 1.5)
        t_corr = accurate_temperature.get_smooth(t_corr)
        if t_corr < cold_temp:
            send_notification_via_pushbullet(temperature_message, head_message)
            time.sleep(sleep_time)

main()