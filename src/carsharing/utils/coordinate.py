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
    return ((coord1.x - coord2.x) ** 2 + (coord1.y - coord2.y) ** 2) ** 0.5
