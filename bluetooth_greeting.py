import bluetooth
from sense_hat import SenseHat
import time

def main():

    MAC_ADDRESS_FILE = open("MAC Addresses.txt", "r")
    while True:
        scan_file(MAC_ADDRESS_FILE)

def scan_file(file):

    for mac in file:
        words = mac.split()
        for word in words:
            print(mac)
    


def send_message(user_name, device_name):

    sense = SenseHat()
    temperature = round(sense.get_temperature(), 1)
    sense.show_message("Hi {}! the temperature today is {}*c".format(user_name, temperature), scroll_speed = 0.05)
    #Send message

main()