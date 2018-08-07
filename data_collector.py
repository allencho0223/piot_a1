import time
import sqlite3
from sense_hat import SenseHat

dbname="sensehat_env.db"
sampleFreq = 1 # time in seconds

# def getHumidity():
# def getTemperature():
# def getPressure():


def getSenseHatData():
    sense = SenseHat()
    temperature = sense.get_temperature()
    humidity = sense.get_humidity()
    pressure = sense.get_pressure()

    if temperature is not None:
        temperature = round(temperature, 1)

    if humidity is not None:
        humidity = round(humidity, 1)

    if pressure is not None:
        pressure = round(pressure, 1)

    putData(humidity, temperature, pressure)
    
    

def putData(humidity, temperature, pressure):
    conn = sqlite3.connect(dbname)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO SENSEHAT_data values(datetime('now'), (?), (?), (?))", (humidity, temperature, pressure))
    conn.commit()
    conn.close()

def displayData():
    conn = sqlite3.connect(dbname)
    curs = conn.cursor()
    print("\nEntire database contents:\n")
    for row in curs.execute("SELECT * FROM SENSEHAT_data"):
        print(row)
    conn.close()
    


def main():
    for i in range(0,3):
        getSenseHatData()
        time.sleep(sampleFreq)
    displayData()

main()
