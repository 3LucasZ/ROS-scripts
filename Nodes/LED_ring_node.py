#! /usr/bin/env python
'''
Turning an LED ring on and off
this relies on: 
    colorSetTrial.py
    colorDeleteTrial.py
so please carefully edit these before using this
'''
import rospy
import RPi.GPIO as GPIO
import time
from std_msgs.msg import Bool
import os

#called when the LED toggle button is pressed or released
def callback_ringLED_toggle(msg):
    if(msg.data == True):
        global ringLEDstatus
        ringLEDstatus = 1 - ringLEDstatus
        if(ringLEDstatus == 1):
            os.system("sudo python3 /home/ubuntu/catkin_ws/src/roboquest/src/LED_ring_set_color.py")
        else:
            os.system("sudo python3 /home/ubuntu/catkin_ws/src/roboquest/src/LED_ring_remove_color.py")

ringLEDstatus = 0

#ROS setup stuff
#Initialize this ROS node
rospy.init_node('ringLEDtoggle')

#setup the subscribers and their callbacks
rospy.Subscriber("ringLED_wanted_state", Bool, callback_ringLED_toggle)

rate = rospy.Rate(20)
while not rospy.is_shutdown():
    rate.sleep()
