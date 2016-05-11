#!/usr/bin/python
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# set desired pin number 
pin = 2
counter = 0
waitingTime = 5
threshold = 4

# init
GPIO.setup(pin, GPIO.OUT, initial=GPIO.LOW)

# toggle pin on/off till loop ends.
while (counter < threshold):
 GPIO.output(pin, GPIO.HIGH) #setting pin output as high | 1 | on
 time.sleep(waitingTime); 
 GPIO.output(pin, GPIO.LOW) #setting pin output as low | 0 | off
 time.sleep(waitingTime);
 counter = counter+1
 
GPIO.cleanup()
