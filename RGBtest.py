import sys, time
import RPi.GPIO as GPIO
redPin   = 19
greenPin = 20
bluePin  = 26

GPIO.setmode(GPIO.BOARD)
def turnOnPin(pin):
     GPIO.setup(pin, GPIO.OUT)
     GPIO.output(pin, GPIO.HIGH)

def turnOffPin(pin):
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)

turnOnPin(redPin)
