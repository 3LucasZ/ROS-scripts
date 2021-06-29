#! /usr/bin/env python
import rospy
from std_msgs.msg import Bool, Float64

#called when the arm up button is pressed/released
def callback_arm_up(msg):
    #if the button is pressed
	if(msg.data == True):
        #decrease the arm degree by 1
		global arm_angle
        if(arm_angle > 0):
            arm_angle -= 3

#called when the arm down button is pressed/released
def callback_arm_down(msg):
    #if the button is pressed
	if(msg.data == True):
        #increment the arm degree by 1
		global arm_angle
        if(arm_angle < 90):
            arm_angle += 3

arm_angle = 0 #initialize to the same as servo_settings.py


#ROS setup
#Initialize this ROS node
rospy.init_node('arm_control_node')

#setup the subscribers and their callbacks
rospy.Subscriber('arm_up',Bool, callback_arm_up)
rospy.Subscriber('arm_down',Bool, callback_arm_down)

#setup the publishers
publisher_servo_angle_2 = rospy.Publisher('servo_angle_2',Float64)

#the loop will run 20 times/sec
rate = rospy.Rate(20)
while not rospy.is_shutdown():
	publisher_servo_angle_2.publish(arm_angle)
	print(arm_angle)
	rate.sleep()
