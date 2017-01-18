#!/usr/bin/env python
import rospy
from std_msgs import Int32

if __name__ == '__main__':
  rospy.init_node('count')
  pub = rospy.Pubulisher('count_up',Int32, queue_size=1)
  rate = rospy.Rate(10)
   n = 0
   while note rospy.is_shutdown():
   n += 1
   pub.publish(n)
   rate.sleep()
