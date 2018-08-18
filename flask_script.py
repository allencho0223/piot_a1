#!/usr/bin/env python3

### Acknowledgements
# Using development environment instead of production
# https://stackoverflow.com/questions/30554702/cant-connect-to-flask-web-service-connection-refused

# Retrieving sqlite3 database into html file with flask
# https://stackoverflow.com/questions/39816944/cannot-get-html-to-display-sqlite3-data-with-python-flask

# Getting UTC time zone and conversion on
# https://www.saltycrane.com/blog/2009/05/converting-time-zones-datetime-objects-python/

# Timezone List on
# https://stackoverflow.com/questions/13866926/is-there-a-list-of-pytz-timezones

# Sqlite3 exception handlings
# https://www.programcreek.com/python/example/6844/sqlite3.Error

# Import packages and other class libraries

from flask import Flask
from flask import render_template
import sqlite3
import os

from flask_moment import Moment
from datetime import datetime
from dateutil import tz
from sense_hat import SenseHat

c = ""
# Connect database
try:
    conn = sqlite3.connect('/home/pi/iot/ass1/sensehat_env.db', 
                            check_same_thread=False)
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
except sqlite3.Error as e:
    print("Database error: %s" % e)
except Exception as e:
    print("Exception occurred in this script: %s" % e)

# Get prepared for flask (a web server) and moment (time conversion)
app = Flask(__name__, static_url_path='/static')
moment = Moment(app)

# Declare arrays for data optimisation
time_data = []
humidity_data = []
temperature_data = []
pressure_data = []
discomfort_data = []


def optimise_data(rows):

    # Get UTC time and local time from dateutil package
    utc_zone = tz.tzutc()
    local_time_zone = tz.tzlocal()

    # Iterate over data from the database
    for row in rows:

        # Convert UTC time to local time
        utc = datetime.strptime(row[0], '%Y-%m-%d %H:%M:%S')
        utc = utc.replace(tzinfo=utc_zone).astimezone(tz=None)
        local_time = utc.astimezone(local_time_zone)
        local_time = datetime.strftime(local_time, '%Y-%m-%d %H:%M:%S')

        # Assign again for future use in flask script
        time_data.append(local_time)
        humidity_data.append(row[1])
        temperature_data.append(row[2])
        pressure_data.append(row[3])
        discomfort_data.append(row[4])


# Execute sqlite query to retrieve data and pass them to flask 
@app.route('/', methods=['GET'])
def index():
    
    c.execute('SELECT * FROM SENSEHAT_DATA;')
    data = c.fetchall()
    optimise_data(data)
    return render_template('flask.html', rows = time_data, hum = humidity_data,
                             temp = temperature_data, press = pressure_data, dis = discomfort_data)


# This module is only run when it is executed by the interpreter itself
if __name__ == "__main__":
    # At home
    # app.run(debug=True, host='0.0.0.0')
    # At university
    app.run(debug=True, host=os.popen('hostname -I').read())
    