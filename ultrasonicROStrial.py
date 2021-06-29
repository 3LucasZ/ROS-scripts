#! /usr/bin/env python
#Libraries
import RPi.GPIO as GPIO
import time
import rospy
import math
from std_msgs.msg import Float32, Float64, String
 
print("Code ran!")
#GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)
 
#set GPIO Pins
GPIO_TRIGGER = 6
GPIO_ECHO = 16
 
#set GPIO direction (IN / OUT)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)
 
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

angle = 0.0
def callback_servo_angle_received(msg):
    global angle
    angle = msg.data

def height(hypotenuse, angle):
    if(angle >= 90):
        return hypotenuse*(math.sin((angle-90)*math.pi/180))+21
    else:
        return 21 - hypotenuse*(math.sin(90-angle)*math.pi/180) 



#setup the publishers
publisher_ultrasonic_distance = rospy.Publisher('ultrasonic_distance',Float32)
publisher_ultrasonic_height = rospy.Publisher('ultrasonic_height',Float32)

#setup the subscriber and its callback
rospy.Subscriber("servo_angle_0", Float64, callback_servo_angle_received)

rospy.init_node("ultrasonicROSTrial")

#rate = rospy.Rate(500)
if __name__ == '__main__':
    try:
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
