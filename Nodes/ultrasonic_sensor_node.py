#! /usr/bin/env python
'''
Publishing on 1 topic: 
    ultrasonic_distance, which measures the distance sensed by the sensor.
    ultrasonic_height, which measures the height of an object based on ultrasonic_distance.
'''
#SETUP
#Libraries, message types used
import RPi.GPIO as GPIO
import time
import rospy
import math
from std_msgs.msg import Float32
#(BOARD / BCM)
GPIO.setmode(GPIO.BCM)
#GPIO Pins (Change if necessary)
GPIO_TRIGGER = 6
GPIO_ECHO = 16
#GPIO direction (IN / OUT)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)
 

#FUNCTIONS
#calculates the current distance sensed
def distance():
    # set Trigger to HIGH
    GPIO.output(GPIO_TRIGGER, True)
 
    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)
 
    StartTime = time.time()
    StopTime = time.time()
 
    # save StartTime
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()
 
    # save time of arrival
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()
 
    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2
 
    return distance


#PUB/SUB
publisher_ultrasonic_distance = rospy.Publisher('ultrasonic_distance',Float32)
#initialize the node
rospy.init_node("ultrasonic_sensor_node")


#RUN
if __name__ == '__main__':
    try:
        print("ultrasonic_sensor_node started")
        while True:
            dist = distance()
            print ("Measured Distance = " + str(dist) + " cm")
            publisher_ultrasonic_distance.publish(dist)
            publisher_ultrasonic_height.publish(h)
            time.sleep(1)
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()
