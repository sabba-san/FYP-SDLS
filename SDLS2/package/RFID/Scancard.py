import RPi.GPIO as gpio
from mfrc522 import SimpleMFRC522

scan = SimpleMFRC522()

def scanning():
    print("test scan")
    
    try:
        id,name = scan.read()
        print("card ID",id)
        print("name:", name)
        
    finally:
            gpio.cleanup()


scanning()