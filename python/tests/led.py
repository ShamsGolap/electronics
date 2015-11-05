#!/usr/bin/python

import RPi.GPIO as GPIO
import time

led_pin = 11

GPIO.setmode(GPIO.BOARD)
GPIO.setup(led_pin, GPIO.OUT)
GPIO.output(led_pin, GPIO.HIGH)

try:
    while True:
        print 'led on'
        GPIO.output(led_pin, GPIO.LOW)
        time.sleep(1)

        print 'led off'
        GPIO.output(led_pin, GPIO.HIGH)
        time.sleep(1)

except KeyboardInterrupt:
    GPIO.output(led_pin, GPIO.HIGH)
    GPIO.cleanup()
