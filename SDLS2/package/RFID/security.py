#!/usr/bin/env python
# -*- coding: utf8 -*-
 
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
from time import sleep

Led = 4
#======================
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(Led,GPIO.OUT)

#======================



continue_reading = True

reader = SimpleMFRC522()




def unlock():
    Tag1 ="109660275408"
    
    door = True
    print("Test lock solenoid")
    
    while True:
        
        print("Place your tag ID:")
        id,Tag =reader.read()
        id =str(id)
        
        if id == Tag1:
            print ("successful")
            
            
            if door == True:
                print("door is open")
                
                #LED
                GPIO.output(Led ,GPIO.HIGH)#on
                sleep(1)                        # 1 TRUE
                GPIO.output(Led, GPIO.LOW) #off
                
                #SOLENOID
                GPIO.output(18, 0)
                sleep(3)
                
                door = False
            
            elif door == False:
                print ("door is lock")
                GPIO.output(Led ,GPIO.HIGH) #on
                sleep(1)
                GPIO.output(Led, GPIO.LOW) #off     #LOCK
                sleep(0.5)
                #SOLENOID
                GPIO.output(18,1)
                sleep(1)
                door = True
                sleep(3)
                
                
        else:
            print("wrong tag")
            #LED
            GPIO.output(Led ,GPIO.HIGH) #on
            sleep(1)
            GPIO.output(Led, GPIO.LOW) #off      #2 FALSE
            sleep(0.5)
            GPIO.output(Led ,GPIO.HIGH) #on
            GPIO.output(Led, GPIO.LOW) #off
            sleep(0.5)
        
            #SOLENOID
            GPIO.output(18,1)
            sleep(1)

unlock()
        
        
        
        