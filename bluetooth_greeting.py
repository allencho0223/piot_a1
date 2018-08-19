#!/usr/bin/env python3

# Import packages
import bluetooth
from sense_hat import SenseHat
import time
from accurate_temperature import return_accuratetemp

# Main function reading registered devices from a text file and displaying messages on the hat
def main():

    try:
        # Alex's workspace
        # MAC_ADDRESS_FILE = open("/home/pi/Assignment1/MAC_Addresses.txt", "r")
        # Allen's workspace
        MAC_ADDRESS_FILE = open("/home/pi/iot/ass1/MAC_Addresses.txt", "r")
        nearby_devices = bluetooth.discover_devices(lookup_names = False)

        # Scan a friendly device nearby the Pi from the text file
        scan_file(nearby_devices,MAC_ADDRESS_FILE)
        
    except IOError:
        print("Error: Could not open file")

# A function retrieving the registered user's mac address and name
def scan_file(nearby_devices,file):
    
    for user in file:
        #Get mac address from user's data in txt file
        mac = user.split(", ")[1]
        for addresses in nearby_devices:

            if addresses in mac:
                #Remove MAC address from line read from file
                name = user.split(",")[0]
                send_message(name)

# Display greeting message and current temperature on the hat's led
def send_message(user_name):

    sense = SenseHat()
    acc_temp = return_accuratetemp()
    temperature = round(acc_temp, 1)
    sense.show_message("Hi {}! the temperature today is {}*c".format(user_name, temperature), scroll_speed = 0.05)

# Main function
main()
