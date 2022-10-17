#!/usr/bin/env python

import time
import RPi.GPIO as gpio
from mfrc522 import SimpleMFRC522
import mysql.connector

db = mysql.connector.connect(
    
    host="localhost",
    user="adminSDLS",
    passwd="sdls",
    database="SDLS"
    
    )
cursor = db.cursor()

reader = SimpleMFRC522()

try:
    while True:
        print("PLACE CARD TO register")
        id,text = reader.read()
        
        cursor.execute("SELECT id FROM Rfid WHERE rfid_uid ="+str(id))
        cursor.fetchone()
        
        if cursor.rowcount >=1:
            print("Overwrite existing user?")
            overwrite = input("Overwrite (Y/N)?")
            
            if overwrite[0] == 'Y' or overwrite[0] == 'y':
                print("Overwrite user")
                time.sleep(1)
                sql_insert = "UPDATE Rfid SET name= %s WHERE rfid_uid=%s"
                
            else:
                continue;
                
        else:
            sql_insert = "INSERT INTO Rfid (name,rfid_uid) VALUES (%s,%s)"
            print("Enter new name:")
            new_name = input("Name:")
            
            cursor.execute(sql_insert, (new_name,id))
            
            db.commit()
            
            print("User" + new_name + "saved")
            time.sleep(2)
finally:
    gpio.cleanup()