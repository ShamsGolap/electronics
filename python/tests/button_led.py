#!/usr/bin/python

import RPi.GPIO as GPIO
import time

led_pin = 11
button = 12

GPIO.setmode(GPIO.BOARD)

GPIO.setup(led_pin, GPIO.OUT)
GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.output(led_pin, GPIO.HIGH)

try:
    while True:
        if GPIO.input(button) == GPIO.LOW:
            print 'led on'
            GPIO.output(led_pin, GPIO.LOW)
        else:
            print 'led off'
            GPIO.output(led_pin, GPIO.HIGH)
except KeyboardInterrupt:
    GPIO.output(led_pin, GPIO.HIGH)
    GPIO.cleanup()
