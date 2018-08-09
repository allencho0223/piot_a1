#!/usr/bin/env python3
import time
import sqlite3
from sense_hat import SenseHat
from timezone import convertTimeZone

# Set absolute path for database
dbname="/home/pi/iot/ass1/sensehat_env.db"

# Declare global sensehat object for various uses
sense = SenseHat()

# Get temperature from sensehat
def getTemperature():
    temperature = sense.get_temperature()
    if temperature is not None:
        temperature = round(temperature, 1)
    return temperature

# Get humidity from sensehat
def getHumidity():
    humidity = sense.get_humidity()    
    if humidity is not None:
        humidity = round(humidity, 1)
    return humidity

# Get pressure from sensehat
def getPressure():
    pressure = sense.get_pressure()
    if pressure is not None:
        pressure = round(pressure, 1)
    return pressure

# Get current measured data and put them into database connected
def getSenseHatData():

    temperature = getTemperature()
    humidity = getHumidity()
    pressure = getPressure()

    putData(humidity, temperature, pressure)

# Put data into the database
def putData(humidity, temperature, pressure):
    conn = sqlite3.connect(dbname)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO SENSEHAT_data values(datetime('now'), (?), (?), (?))", (humidity, temperature, pressure))
    conn.commit()
    conn.close()

# Display data stored in the database for debugging
def displayData():
    conn = sqlite3.connect(dbname)
    curs = conn.cursor()
    print("\nEntire database contents:\n")
    for row in curs.execute("SELECT * FROM SENSEHAT_data"):
        print(row)
    conn.close()

# Main function
def main():
    for i in range(0,3):
        getSenseHatData()
    displayData()

# Call main function
main()
