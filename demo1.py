#!/usr/bin/python
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# set desired pin number 
pin = 2

# init
GPIO.setup(pin, GPIO.OUT)
GPIO.output(pin, GPIO.HIGH)
time.sleep(waitingTime);

GPIO.output(pin, GPIO.LOW)
time.sleep(waitingTime); 

GPIO.cleanup()
