#! /usr/bin/env python
import rospy
import RPi.GPIO as GPIO
import time
from std_msgs.msg import Bool

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(26,GPIO.OUT)

#called when the LED toggle button is pressed or released
def callback_LED_toggle(msg):
    if(msg.data == True):
        global LEDstatus
        LEDstatus = 1 - LEDstatus

LEDstatus = 0

#ROS setup stuff
#Initialize this ROS node
rospy.init_node('LEDtoggle')

#setup the subscribers and their callbacks
rospy.Subscriber("LED_wanted_state", Bool, callback_LED_toggle)

rate = rospy.Rate(20)
while not rospy.is_shutdown():
    if(LEDstatus == 1):
        GPIO.output(26,GPIO.HIGH)
    else:
	GPIO.output(26,GPIO.LOW)
    rate.sleep()
