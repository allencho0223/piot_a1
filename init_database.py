import sqlite3 as lite
import sys
con = lite.connect('sensehat_env.db')
with con: 
    cur = con.cursor() 
    cur.execute("DROP TABLE IF EXISTS SENSEHAT_data")
    cur.execute("CREATE TABLE SENSEHAT_data(timestamp DATETIME, humidity NUMERIC, temperature NUMERIC, pressure NUMERIC)")
