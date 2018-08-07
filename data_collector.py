import time
import sqlite3
from sense_hat import SenseHat

dbname="sensehat_env"

# def getHumidity():
# def getTemperature():
# def getPressure():
    

def putData(humidity, temperature, pressure):
    conn=sqlite3.connect(dbname)
    cursor=conn.cursor()
    cursor.execute("INSERT INTO SENSEHAT_data values(datetime('now'), (?), (?), (?),", (humidity, temperature, pressure))
    sensehat_env.commit()


def main():
    sense=SenseHat()
    humidity = sense.get_Humidity
    temperature = sense.get_Temperature
    pressure = sense.get_Pressure
    putData(humidity, temperature, pressure)
