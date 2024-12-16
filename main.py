import datetime
from random import randint
import serial
import time
import RPi.GPIO as GPIO
import requests

def GetMoisture():
    arduino = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
    time.sleep(2) #venter på adgang til arduino
    dry = 520
    wet = 260
    try:
        data = arduino.readline().decode().strip()
        if data:
            raw = int(data)
            moisture = (dry-raw)/(dry-wet)*100
            arduino.close()
            return moisture
        time.sleep(2)
    finally:
        arduino.close()
        return 0

def PumpRelay():
        GPIO.output(25, GPIO.HIGH)  #tænd pumpe
        time.sleep(5)               #lader pumpen pumpe
        GPIO.output(25, GPIO.LOW)   #sluk pumpe


###########################
#       get data from db
#getrequest om planteid, desiredmoisture

###########################
#       send data to db
#
#Collecting data for transfer
# plantID = variabel fra db
# time = datetime.datetime.now()
# moisture = GetMoisture()
# remainingWater = randint(1,100)     #placeholder indtil ultrasonisk sensor virker
#
#postrequest til rest med variabler

###########################
#       Auto pump feature
#if desiredmoisture > moisture:
#   PumpRelay()

###########################
#       schedule
# while 1:
#loop med if statements for
#hvornår pi'en skal kalde
#forskellige funktioner
#
#f.eks. hvis datetime.datetime.now().minute = 00
#skal der oprettes en log og den skal sendes
#til db





