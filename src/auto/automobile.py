from enum import Enum


class AutomobileState(Enum):
    OCCUPIED = 0,
    AVAILABLE = 1,
    SUSPENDED = 2


class Automobile(object):
    def __init__(self):
        pass

    def open_vehicle(self):
        pass

    def close_vehicle(self):
        pass
