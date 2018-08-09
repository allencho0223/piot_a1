from sense_hat import SenseHat
import requests
import json
import time
import os
 
def send_notification_via_pushbullet(title, body):
    """ Sending notification via pushbullet.
        Args:
            title (str) : title of text.
            body (str) : Body of text.
    """
    data_send = {"type": "note", "title": title, "body": body}
 
    ACCESS_TOKEN = 'o.gmSIfrIUwZwFFGrQlLYU8tkRW116p3k3'
    resp = requests.post('https://api.pushbullet.com/v2/pushes', data=json.dumps(data_send),
                         headers={'Authorization': 'Bearer ' + ACCESS_TOKEN, 'Content-Type': 'application/json'})
    if resp.status_code != 200:
        raise Exception('Something wrong')
    else:
        print('complete sending')      
def get_cpu_temp():
    res = os.popen("vcgencmd measure_temp").readline()
    t = float(res.replace("temp=", "").replace("'C\n", ""))
    return(t)

# use moving average to smooth readings
def get_smooth(x):
    if not hasattr(get_smooth, "t"):
        get_smooth.t = [x, x, x]
    get_smooth.t[2] = get_smooth.t[1]
    get_smooth.t[1] = get_smooth.t[0]
    get_smooth.t[0] = x
    xs = (get_smooth.t[0]+get_smooth.t[1]+get_smooth.t[2])/3
    return(xs)

def returnAccurateTemp():
    sense=SenseHat()
    t1 = sense.get_temperature_from_humidity()
    t2 = sense.get_temperature_from_pressure()
    t_cpu = get_cpu_temp()
    h = sense.get_humidity()
    p = sense.get_pressure()

    # calculates the real temperature compesating CPU heating
    t = (t1 + t2) / 2
    t_corr = t - ((t_cpu - t) / 1.5)
    t_corr = get_smooth(t_corr)
    
    return t_corr

def main():
    
    message = "You should bring a jacket."
    sleep_time = 300  #Change to 300 (5 minutes)
    temperature_message = "It is less than 20 degrees"
    sense = SenseHat()

    cold_temp=20
    run = 0
    while run < 1:
        t1 = sense.get_temperature_from_humidity()
        t2 = sense.get_temperature_from_pressure()
        t_cpu = get_cpu_temp()
        t = (t1 + t2) / 2
        t_corr = t - ((t_cpu - t) / 1.5)
        t_corr = get_smooth(t_corr)
        if t_corr < cold_temp:
            send_notification_via_pushbullet(temperature_message, message)
            time.sleep(sleep_time)

main()