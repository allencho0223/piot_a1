### Acknowledgements
# Using development environment instead of production
# https://stackoverflow.com/questions/30554702/cant-connect-to-flask-web-service-connection-refused
# Retrieving sqlite3 database into html file with flask
# https://stackoverflow.com/questions/39816944/cannot-get-html-to-display-sqlite3-data-with-python-flask

from flask import Flask
from flask import render_template
import sqlite3

conn = sqlite3.connect('/home/pi/iot/ass1/sensehat_env.db', check_same_thread=False)
conn.row_factory = sqlite3.Row
c = conn.cursor()
app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    
    c.execute('SELECT * FROM SENSEHAT_DATA;')
    return render_template('flask.html', rows = c.fetchall())

#@app.route('/')
#def index():
#    return "hello world"

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
