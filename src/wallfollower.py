#!/usr/bin/python3
import rospy
from FSM import States

def main():
    rospy.init_node('wallfollwer_node')
    sm = States()
    sm.current_state = States.STATE_INIT

