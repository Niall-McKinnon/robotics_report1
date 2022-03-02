#!/usr/bin/env python3

import rospy
import math

# import the plan message
from ur5e_control.msg import Plan
from geometry_msgs.msg import Twist

# define a function that defines a new point
def add_point(plan, linX, linY, linZ, anX, anY, anZ):
		plan_point = Twist()
		
		plan_point.linear.x = linX
		plan_point.linear.y = linY
		plan_point.linear.z = linZ
		plan_point.angular.x = anX
		plan_point.angular.y = anY
		plan_point.angular.z = anZ
		
		plan.points.append(plan_point)

if __name__ == '__main__':
	# initialize the node
	rospy.init_node('custom_planner', anonymous = True)
	# add a publisher for sending joint position commands
	plan_pub = rospy.Publisher('/plan', Plan, queue_size = 10)
	# set a 10Hz frequency for this loop
	loop_rate = rospy.Rate(10)

	# define a plan variable
	plan = Plan()
	
	# define the first point
	add_point(plan, -0.5, -0.133, 0.5, 3.14, 0.0, 1.57)
	
	# define the second point
	add_point(plan, -0.5, -0.133, 0.0, 3.14, 0.0, 1.57)
	
	# define the third point
	add_point(plan, -0.5, -0.5, 0.5, 3.14, 0.0, 1.57)
	
	# define the fourth point
	add_point(plan, -0.5, -0.5, 0.0, 3.14, 0.0, 1.57)

	while not rospy.is_shutdown():
		# publish the plan
		plan_pub.publish(plan)
		# wait for 0.1 seconds until the next loop and repeat
		loop_rate.sleep()
