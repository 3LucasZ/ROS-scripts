#! /usr/bin/env python
'''
Publishing on 1 topic: 
    object_height

Subscribing to 2 topics:
    servo_angle_0 (tilt servo)
    ultrasonic_distance
'''
#SETUP
#Libraries, message types used
import time
import rospy
import math
from std_msgs.msg import Float64
tiltAngle = 0.0
distance = 0


#CALLBACKS
def callback_servo_angle(msg):
    global tiltAngle
    tiltAngle = msg.data
def callback_ultrasonic_distance(msg):
    global distance
    distance = msg.data


#FUNCTIONS
#calculates the height of an object
def get_height(hypotenuse, angle):
    if(angle >= 90):
        return hypotenuse*(math.sin((angle-90)*math.pi/180))+21 #Note: 21 is the height of the robot I was using.
    else:
        return 21 - hypotenuse*(math.sin(90-angle)*math.pi/180) 


#PUB/SUB
publisher_ultrasonic_height = rospy.Publisher('ultrasonic_height',Float32)
rospy.Subscriber("ultrasonic_distance", Float64, callback_ultrasonic_distance)
rospy.Subscriber("servo_angle_0", Float64, callback_servo_angle)


#RUN
if __name__ == '__main__':
    try:
        print("object height node started")
        while True:
            height = get_height(distance, tiltAngle)
            print ("Distance: " + str(distance) + " cm")
            print ("Angle: " + str(angle) + " deg")
            print ("Height:  = " + str(height) + " cm")
            publisher_ultrasonic_height.publish(height)
            time.sleep(1)
    except KeyboardInterrupt:
        print("Measurement stopped by User")