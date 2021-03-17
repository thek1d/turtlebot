from enum import Enum, auto

class States(Enum):

    STATE_INIT = auto()
    STATE_DRIVE_STRAIGHT = auto()
    STATE_ROTATE_CCW = auto()
    STATE_TURN_LEFT = auto
    STATE_TURN_RIGHT = auto()
    STATE_STOP = auto()

    def __init__(self):
        self.__State = None
    
    @property
    def current_state(self):
        return self.__State
    
    @Scurrent_state.setter
    def current_state(self, state):
        self.__State = state
    
    def init(self):
        pass
    
    def drive_straight(self):
        pass

    def rotate_ccw(self):
        pass

    def turn_left(self):
        pass

    def turn_right(self):
        pass

    def stop(self):
        pass


