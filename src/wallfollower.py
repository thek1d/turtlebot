#!/usr/bin/python3
import rospy
from fsm import States



def main():
    rospy.init_node('wallfollwer_node')
    rospy.spin()

    while not rospy.is_shutdown():
        pass

if __name__ == '__main__':
    main()

