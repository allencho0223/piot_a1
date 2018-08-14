import bluetooth
from sense_hat import SenseHat
import time

def main():
    
    register_bool = input ("Do you wish to register a device? [Y/N] ")
    if register_bool == 'Y':
        draw_bluetooth()
        register()

def search_device(user_name, device_name):

    print("Searching for your device ({})".format(device_name))
    device_address=None
    nearby_devices = bluetooth.discover_devices()
    for mac_address in nearby_devices:
        device_address = mac_address
        if device_name == bluetooth.lookup_name(mac_address):
            device_address = mac_address
            break

    if device_address is not None:
        print("{}, we found your device!".format(user_name))
        send_message(user_name, device_name)
            
def send_message(user_name, device_name):

    sense = SenseHat()
    temperature = round(sense.get_temperature(), 1)
    sense.show_message("Hi {}! the temperature today is {}*c".format(user_name, temperature), scroll_speed = 0.05)
    #Send message

def register():

    user_name = input ("Please enter your name: ")
    device_name = input ("Please enter the name of your device: ")
    search_device(user_name, device_name)

def draw_bluetooth():
    B = [0, 0, 255]  # Blue
    O = [255, 255, 255]  # White
    sense = SenseHat()
    bluetooth_logo = [
    O, O, O, B, O, O, O, O,
    O, O, O, B, B, O, O, O,
    O, B, O, B, O, B, O, O,
    O, O, B, B, B, O, O, O,
    O, B, O, B, O, B, O, O,
    O, O, O, B, B, O, O, O,
    O, O, O, B, O, O, O, O,
    O, O, O, O, O, O, O, O
    ]
    sense.set_pixels(bluetooth_logo)

    time.sleep(2)
    sense.clear()

main()