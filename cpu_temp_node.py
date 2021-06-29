#! /usr/bin/env python
import rospy
from gpiozero import CPUTemperature
from std_msgs.msg import Float32

rospy.init_node('cputemp')

publisher = rospy.Publisher('cputemp',Float32,queue_size = 1)
rate = rospy.Rate(1) #1 hz

while not rospy.is_shutdown():
	cpu = CPUTemperature()	
	publisher.publish(cpu.temperature)
	rate.sleep()


