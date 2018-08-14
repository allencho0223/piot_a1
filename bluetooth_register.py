import bluetooth
from sense_hat import SenseHat
import time

def main():

    global MAC_ADDRESS_FILE
    MAC_ADDRESS_FILE = open("MAC Addresses.txt","a+")
    register_bool = input ("Do you wish to register a device? [Y/N] ").upper()
    if register_bool == 'Y':
        
        draw_bluetooth()
        register()
    MAC_ADDRESS_FILE.close()

def search_device(user_name, device_name, max_address_file):

    print("Searching for your device ({})".format(device_name))
    sense = SenseHat()
    sense.clear()
    device_address=None
    nearby_devices = bluetooth.discover_devices()
    for mac_address in nearby_devices:
        device_address = mac_address
        if device_name == bluetooth.lookup_name(mac_address):
            device_address = mac_address
            break

    if device_address is not None:
        MAC_ADDRESS_FILE.write("{}, {}, {}\r\n".format(user_name, device_name, mac_address))
        print("{}, your device '{}' has been registered!".format(user_name, device_name))
        send_message(user_name, device_name)
        
            
def send_message(user_name, device_name):

    sense = SenseHat()
    temperature = round(sense.get_temperature(), 1)
    sense.show_message("Hi {}! the temperature today is {}*c".format(user_name, temperature), scroll_speed = 0.05)
    #Send message

def register():

    user_name = input ("Please enter your name: ")
    device_name = input ("Please enter the name of your device: ")
    search_device(user_name, device_name, MAC_ADDRESS_FILE)

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

main()