#!/usr/bin/python

import RPi.GPIO as GPIO
import time

REVERSE = True
pins = [11, 12, 13, 15, 16, 18, 22, 7]

if REVERSE:
    pins = pins[::-1]

def setup():
    GPIO.setmode(GPIO.BOARD)

    for pin in pins:
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, GPIO.HIGH)

    for i in range(3):
        for pin in pins:
            time.sleep(0.05)
            GPIO.output(pin, GPIO.LOW)

        for pin in pins:
            time.sleep(0.05)
            GPIO.output(pin, GPIO.HIGH)        

def loop():
    value = copy_value = 0
    bits = [1, 2, 4, 8, 16, 32, 64, 128][::-1]
    binary = [1, 1, 1, 1, 1, 1, 1, 1]

    while True:
        while copy_value > 0:
            for key, bit in enumerate(bits):
                if copy_value - bit < 0:
                    binary[key] = 1
                else:
                    binary[key] = 0
                    copy_value -= bit

        for index, pin in enumerate(pins):
            GPIO.output(pin, binary[index])

        time.sleep(1)

        value += 1
        copy_value = value

        if value == 256:
            value = copy_value = 0

def destroy():
    for pin in pins:
        GPIO.output(pin, GPIO.HIGH)

    GPIO.cleanup()


if __name__ == '__main__':
    try:
        setup()
        loop()
    except KeyboardInterrupt:
        destroy()