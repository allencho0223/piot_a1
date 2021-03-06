#!/usr/bin/env python3
### Acknowledgements
# Source files for retrieving data (humidity, temperature, pressure) are given by RMIT PIoT staff
# Formula to calculate discomfort index
# https://keisan.casio.com/exec/system/1351058230

# Import python packages
import sqlite3
from sense_hat import SenseHat
from accurate_temperature import return_accuratetemp

# Declare a variable for global uses
dbname = ""
sense = SenseHat()

# Set absolute path for database
try:
    dbname = "/home/pi/iot/ass1/sensehat_env.db"
except sqlite3.Error:
    print("Can't open database file.")


# Get temperature from sensehat
def retrieve_temperature():
    temperature = return_accuratetemp()
    if temperature is not None:
        temperature = round(temperature, 1)
    return temperature


# Retrieve discomfort index
def retrieve_discomfort_index():
    temperature = retrieve_temperature()
    humidity = retrieve_humidity()
    discomfort = temperature - 0.55 * (1 - 0.01 * (humidity)) * (temperature - 14.5)
    if discomfort is not None:
        discomfort = round(discomfort, 1)
    return discomfort


# Get humidity from sensehat
def retrieve_humidity():
    humidity = sense.get_humidity()    
    if humidity is not None:
        humidity = round(humidity, 1)
    return humidity


# Get pressure from sensehat
def retrieve_pressure():
    pressure = sense.get_pressure()
    if pressure is not None:
        pressure = round(pressure, 1)
    return pressure


# Get current measured data and put them into database connected
def get_sensehat_data():

    temperature = retrieve_temperature()
    humidity = retrieve_humidity()
    pressure = retrieve_pressure()
    discomfort = retrieve_discomfort_index()

    # Put data into the database connected
    put_data(humidity, temperature, pressure, discomfort)


# Put data into the database
def put_data(humidity, temperature, pressure, discomfort):

    conn = sqlite3.connect(dbname)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO SENSEHAT_data values(datetime('now'), (?), (?), (?), (?))", 
                    (humidity, temperature, pressure, discomfort))
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
    get_sensehat_data()
    display_data()


# Call main function
main()
