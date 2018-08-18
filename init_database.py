#!/usr/bin/env python3

### Acknowledgements
# Database connection script is from PIoT lab 4 code archive of RMIT

# Import packages
import sqlite3
import sys

# Connect to the database
try:
    con = sqlite3.connect('sensehat_env.db')
except sqlite3.Error:
    print("Can't open database file.")


# Run queries
with con: 
    cur = con.cursor() 
    cur.execute("DROP TABLE IF EXISTS SENSEHAT_data")
    cur.execute("CREATE TABLE SENSEHAT_data(timestamp DATETIME, humidity NUMERIC, temperature NUMERIC, pressure NUMERIC, discomfort NUMERIC)")
