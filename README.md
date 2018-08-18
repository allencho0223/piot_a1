# piot_a1
RMIT Semester 2, 2018 Programming Internet of Things Assignment 1<br/>

Language: Python<br/>
Device: Raspberry Pi with SenseHAT<br/>
Functionalities: To be added.<br/>

Developers

- Allen(Minyoung) Cho
- Alex Ryland

Script descriptions

- accurate_temperature.py
    - Due to the heat generated from the Pi's cpu, it's hard to retrieve the accurate temperature.
    - So that a developer used some formula to retrieve the accurate temperature
- bluetooth_greeting.py
    - iterate the registered devices and connect to a device nearby
    - Display greeting message and temperature on sense hat
- bluetooth_rgister.py
    - Ask a device to register  
    - Save registered data (name, and the device name) into a text file
- data_collector.py
    - Retrieve some data (humidity, pressure, temperature, and discomfort index) from the Pi
    - Store them into sqlite3 table
- data_shell_script.sh
    - A bash script running data_collector.py every 5 seconds
    - Runs 12 times (a minute)
- flask_script.py
    - Retrieve data from sqlite3
    - Send data to html for data representation
    - Convert UTC to local timezone
- init_database.py
    - Initialise database
    - Remove the database and create a new one if exists
- pushbullet_notifiation.py
    - Send pushbullet notification through a device with appropriate access token
    - Sends every 5 minutes (can be changed to shorter term for testing purpose)
- static/draw_chart.js
    - Draw a chart for data representation
    - Using an external javascript to avoid code repetition
- static/style.css
    - Used for simple html table design
- templates/flask.html
    - A web interface script
    - Display data graphs and tables
    - Use jinja2 syntax to retrieve data from sqlite3
