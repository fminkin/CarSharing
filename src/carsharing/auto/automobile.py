from enum import Enum


class AutomobileState(Enum):
    OCCUPIED = 0,
    AVAILABLE = 1,
    SUSPENDED = 2


class VehicleState(Enum):
    ECONOM = 0,
    COMFORT = 1,
    BUSINESS = 2


class Automobile(object):
    def __init__(self):
        self.mark = None
        self.capacity = None
        self.car_system = None
        self.vehicle_class = None
        self.auto_state = None
        self.automobile_coordinate = None

    def open_vehicle(self):
        pass

    def close_vehicle(self):
        pass
