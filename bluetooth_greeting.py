import bluetooth
from sense_hat import SenseHat
import time

def main():

    try:
        MAC_ADDRESS_FILE = open("MAC Addresses.txt", "r")
        #Infinite loop
        while True:
            scan_file(MAC_ADDRESS_FILE)
    except IOError:
        print("Error: Could not open file")

def scan_file(file):

    for mac in file:
        #Remove MAC address from line read from file
        name = mac.split(",")[0]
        send_message(name)

def send_message(user_name):

    sense = SenseHat()
    temperature = round(sense.get_temperature(), 1)
    sense.show_message("Hi {}! the temperature today is {}*c".format(user_name, temperature), scroll_speed = 0.05)

main()