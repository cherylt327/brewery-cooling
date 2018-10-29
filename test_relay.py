#!/usr/bin/python
from RPi import GPIO
import time
GPIO.setmode(GPIO.BCM)

pins = [6,5,10,22,27,17,9,11]
for pin in pins:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.HIGH)
SleeTimeL = 2

count = 1
for pin in pins:
    GPIO.output(pin, GPIO.LOW)
    print count
    time.sleep(SleeTimeL)
    count +=1
GPIO.cleanup()
print("DONE")

