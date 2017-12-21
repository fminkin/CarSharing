import time


class Coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y


class TimedCoordinate(object):
    def __init__(self, coordinate):
        self.coordinate = coordinate
        self.timestamp = time.time()


def distance(coord1, coord2):
    return 5 # why????