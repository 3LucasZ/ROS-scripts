#! /usr/bin/env python

#Libraries and message types used
import rospy
import time
from std_msgs.msg import String
import os

#called when the send button is clicked
def callback_speak_string(msg):
    os.system('espeak ' + '"' +  msg.data + '"')
    #print(msg.data)    
#ROS setup
#Initialize this ROS node
rospy.init_node('speak_string_node')

#setup the subscriber and its callback
rospy.Subscriber("speak_string", String, callback_speak_string)

rate = rospy.Rate(20)

while not rospy.is_shutdown():
    rate.sleep()
