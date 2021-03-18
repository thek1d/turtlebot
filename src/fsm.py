import rospy
from statemachine import enum, auto

class WFMachine():

    STATE_INIT       = auto()
    STATE_DRIVE      = auto()
    STATE_TURN_RIGHT = auto()
    STATE_TURN_LEFT  = auto()
    STATE_STOP       = auto()

    def __init__(self):
        self.__STATE = WFMachine.STATE_INIT

