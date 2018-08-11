#!/usr/bin/env python3
import time
import sqlite3
from sense_hat import SenseHat
from accurate_temperature import return_accuratetemp

# Set absolute path for database
dbname="/home/pi/iot/ass1/sensehat_env.db"

# Declare global sensehat object for various uses
sense = SenseHat()

# Get temperature from sensehat
def get_temperature():
    temperature = return_accuratetemp()
    if temperature is not None:
        temperature = round(temperature, 1)
    return temperature

def get_discomfort_index():
    temperature = get_temperature()
    humidity = get_humidity()
    discomfort = temperature - 0.55 * (1 - 0.01 * (humidity)) * (temperature - 14.5)
    if discomfort is not None:
        discomfort = round(discomfort, 1)
    return discomfort

# Get humidity from sensehat
def get_humidity():
    humidity = sense.get_humidity()    
    if humidity is not None:
        humidity = round(humidity, 1)
    return humidity

# Get pressure from sensehat
def get_pressure():
    pressure = sense.get_pressure()
    if pressure is not None:
        pressure = round(pressure, 1)
    return pressure

# Get current measured data and put them into database connected
def get_sensehat_data():

    temperature = get_temperature()
    humidity = get_humidity()
    pressure = get_pressure()
    discomfort = get_discomfort_index()

    put_data(humidity, temperature, pressure, discomfort)

# Put data into the database
def put_data(humidity, temperature, pressure, discomfort):

    conn = sqlite3.connect(dbname)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO SENSEHAT_data values(datetime('now'), (?), (?), (?), (?))"
                    , (humidity, temperature, pressure, discomfort))
    conn.commit()
    conn.close()

# Display data stored in the database for debugging
def display_data():
    conn = sqlite3.connect(dbname)
    curs = conn.cursor()
    print("\nEntire database contents:\n")
    for row in curs.execute("SELECT * FROM SENSEHAT_data"):
        print(row)
    conn.close()

# Main function
def main():
#    for i in range(0,3):
#        get_sensehat_data()
    get_sensehat_data()
    display_data()

# Call main function
main()
