# Import packages
import bluetooth
from sense_hat import SenseHat
import time

# main function
def main():

    global MAC_ADDRESS_FILE
    try:
        MAC_ADDRESS_FILE = open("MAC_Addresses.txt","a+")
        draw_bluetooth()
        register()
    except IOError:
        print("Error: Could not open file")
    MAC_ADDRESS_FILE.close()

# A function finding registered devices nearby the Pi
def search_device(user_name, device_name, max_address_file):

    print("Searching for your device ({})".format(device_name))
    sense = SenseHat()
    sense.clear()
    device_address=None
    nearby_devices = bluetooth.discover_devices()
    for mac_address in nearby_devices:
        if device_name == bluetooth.lookup_name(mac_address):
            device_address = mac_address
            break

    if device_address is not None:
        MAC_ADDRESS_FILE.write("{}, {}\r\n".format(user_name, mac_address))
        print("{}, your device '{}' has been registered!".format(user_name, device_name))
    elif device_address is None:
        print("Could not find {}". format(device_name))

# A function retriving and saving registered user's details
def register():

    user_name = input ("Please enter your name: ")
    device_name = input ("Please enter the name of your device: ")
    search_device(user_name, device_name, MAC_ADDRESS_FILE)

# Display bluetooth logo on the sense hat's led
def draw_bluetooth():
    B = [0, 0, 255]  # Blue
    O = [255, 255, 255]  # White
    sense = SenseHat()
    bluetooth_logo = [
        O, O, O, O, O, O, O, O,
        O, O, O, B, O, O, O, O,
        O, O, O, B, B, O, O, O,
        O, B, O, B, O, B, O, O,
        O, O, B, B, B, O, O, O,
        O, B, O, B, O, B, O, O,
        O, O, O, B, B, O, O, O,
        O, O, O, B, O, O, O, O
    ]
    sense.set_pixels(bluetooth_logo)

# Call main function
main()