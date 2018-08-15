#!/usr/bin/env python3

### Acknowledgements
# Using development environment instead of production
# https://stackoverflow.com/questions/30554702/cant-connect-to-flask-web-service-connection-refused
# Retrieving sqlite3 database into html file with flask
# https://stackoverflow.com/questions/39816944/cannot-get-html-to-display-sqlite3-data-with-python-flask
# Getting UTC time zone and conversion on - https://www.saltycrane.com/blog/2009/05/converting-time-zones-datetime-objects-python/
# Timezone List on - https://stackoverflow.com/questions/13866926/is-there-a-list-of-pytz-timezones

from flask import Flask
from flask import render_template
import sqlite3
import os
from flask_moment import Moment
from datetime import datetime
from dateutil import tz
from pytz import timezone
from sense_hat import SenseHat

conn = sqlite3.connect('/home/pi/iot/ass1/sensehat_env.db', check_same_thread=False)
conn.row_factory = sqlite3.Row
c = conn.cursor()

app = Flask(__name__, static_url_path='/static')
moment = Moment(app)

adjusted_rows = []
humidity_data = []
temperature_data = []
pressure_data = []
discomfort_data = []

def time_convert(rows):
    # iterate over rows
    utc_zone = tz.tzutc()
    local_time_zone = tz.tzlocal()

    for row in rows:

        utc = datetime.strptime(row[0], '%Y-%m-%d %H:%M:%S')
        utc = utc.replace(tzinfo=utc_zone).astimezone(tz=None)
        local_time = utc.astimezone(local_time_zone)
        local_time = datetime.strftime(local_time, '%Y-%m-%d %H:%M:%S')

        adjusted_rows.append(local_time)

        humidity_data.append(row[1])
        temperature_data.append(row[2])
        pressure_data.append(row[3])
        discomfort_data.append(row[4])


    # use datetime to conver to local
    return adjusted_rows


@app.route('/', methods=['GET'])
def index():
    
    c.execute('SELECT * FROM SENSEHAT_DATA;')
    data = c.fetchall()
    time_data = time_convert(data)
    return render_template('flask.html', rows = time_data, hum = humidity_data,
                             temp = temperature_data, press = pressure_data, dis = discomfort_data)

if __name__ == "__main__":
    # At home
    # app.run(debug=True, host='0.0.0.0')
    # At university
    app.run(debug=True, host=os.popen('hostname -I').read())