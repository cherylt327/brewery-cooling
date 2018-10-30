#!/usr/bin/python
from RPi import GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()
pins = [6,5,10,22,27,17,9,11]
for pin in pins:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)
    time.sleep(2)
GPIO.cleanup()

#for pin in pins:
#    GPIO.output(pin, GPIO.LOW)
#    time.sleep(SleeTimeL)
#GPIO.cleanup()
print("DONE")

