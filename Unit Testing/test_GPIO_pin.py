'''
Test power on and off on any GPIO
Python2
'''
import RPi.GPIO as GPIO
import time

#change pin
PIN = 26

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(PIN,GPIO.OUT)
print "Power supplied"
GPIO.output(PIN,GPIO.HIGH)
time.sleep(1)
print "Power not supplied"
GPIO.output(PIN,GPIO.LOW)
