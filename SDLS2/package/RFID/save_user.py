#!/usr/bin/env python

import time
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import mysql.connector
#import Adafruit_CharLCD as LCD

db = mysql.connector.connect(
  host="localhost",
  user="AdminSDLS",
  passwd="SDLS",
  database="RFID"
)

cursor = db.cursor()
reader = SimpleMFRC522()
#lcd = LCD.Adafruit_CharLCD(4, 24, 23, 17, 18, 22, 16, 2, 4);

try:
  while True:
    print('Place Card to\nregister')
    cursor.execute("SELECT id FROM users WHERE rfid_uid="+str(id))
    cursor.fetchone()

    if cursor.rowcount >= 1:
      print("Overwrite\nexisting user?")
      overwrite = input("Overwite (Y/N)? ")

      if overwrite[0] == 'Y' or overwrite[0] == 'y':
        lcd.message("Overwriting user.")
        sql_insert = "UPDATE users SET name = %s WHERE rfid_uid=%s"
      else:

        continue;
    else:
      sql_insert = "INSERT INTO users (name, rfid_uid) VALUES (%s, %s)"
    print('Enter new name')
    new_name = input("Name: ")

    cursor.execute(sql_insert, (new_name, id))

    db.commit()

    print("User " + new_name + "\nSaved")

finally:
  GPIO.cleanup()
