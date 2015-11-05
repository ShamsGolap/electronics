#!/usr/bin/python

import RPi.GPIO as GPIO
import time

if __name__ == '__main__':

    pins = [11, 12, 13, 15, 16, 18, 22, 7]

    GPIO.setmode(GPIO.BOARD)

    for pin in pins:
        GPIO.setup(pin, GPIO.OUT)

    for pin in pins:
        GPIO.output(pin, 0)

    time.sleep(0.5)

    for pin in pins:
        GPIO.output(pin, 1)

    print 'All cleared!'

    GPIO.cleanup()