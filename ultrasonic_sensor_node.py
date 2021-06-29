#! /usr/bin/env python
'''
This is a node for a standard ultrasonic sensor.
Please read the README file for information on the ultrasonic sensor used.
The ultrasonic sensor in this example will have the TRIGGER pin at pin 6 and ECHo pin at pin 16. 
Please change this if necessary.

This node will publish on 2 topics: 
    ultrasonic_distance, which measures the distance sensed by the sensor.
    ultrasonic_height, which measures the height of an object based on ultrasonic_distance.

This node will subscribe to 1 topic:
    servo_angle_0, which measures the tilt of the servo the ultrasonic sensor is attached to.
    Please change this topic name to the name of the topic you are using for the servo.
'''

#Libraries and message types used
import RPi.GPIO as GPIO
import time
import rospy
import math
from std_msgs.msg import Float32, Float64, String
 
#GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)
 
#set GPIO Pins
GPIO_TRIGGER = 6
GPIO_ECHO = 16
 
#set GPIO direction (IN / OUT)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)
 
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

# initialize the angle variable globally
angle = 0.0

# callback for getting the angle of the tilt servo
def callback_servo_angle_received(msg):
    global angle
    angle = msg.data

#calculates the height of an object based on the tilt of the ultrasonic's servo
def height(hypotenuse, angle):
    if(angle >= 90):
        return hypotenuse*(math.sin((angle-90)*math.pi/180))+21 #Note: 21 is the height of the robot I was using.
    else:
        return 21 - hypotenuse*(math.sin(90-angle)*math.pi/180) 

#setup the publishers
publisher_ultrasonic_distance = rospy.Publisher('ultrasonic_distance',Float32)
publisher_ultrasonic_height = rospy.Publisher('ultrasonic_height',Float32)

#setup the subscriber and its callback
rospy.Subscriber("servo_angle_0", Float64, callback_servo_angle_received)

#initialize the node
rospy.init_node("ultrasonicROSTrial")

#rate = rospy.Rate(500)
if __name__ == '__main__':
    try:
        print("ultrasonic sensor node has started successfully!")
        while True:
            dist = distance()
            print ("Measured Distance = " + str(dist) + " cm")
            h = height(dist,angle)
            print ("Measured Height = " + str(h) + " cm")
            print ("Measured Angle = " + str(angle) + " deg")
            publisher_ultrasonic_distance.publish(dist)
            publisher_ultrasonic_height.publish(h)
            time.sleep(1)
 
    # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()
