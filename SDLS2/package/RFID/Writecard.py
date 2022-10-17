#!/usr/bin/env python
import RPi.GPIO as gpio
from mfrc522 import SimpleMFRC522

scannner = SimpleMFRC522()

def detect():
    print ("detect card")
    
    try:
        text=input("NAME:")
        print("Place your card at scanner")
        scannner.write(text)
        print("registered")
        
    finally:
        gpio.cleanup()
        

detect()