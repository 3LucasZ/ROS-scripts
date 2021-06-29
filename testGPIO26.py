'''
Simple script to test if GPIO26 is working.
Here we are supplying GPIO26 with power for 1 second.
'''
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(26,GPIO.OUT)
print "Power supplied"
GPIO.output(26,GPIO.HIGH)
time.sleep(1)
print "Power not supplied"
GPIO.output(26,GPIO.LOW)
