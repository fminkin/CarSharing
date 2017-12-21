from enum import Enum
from src.contrib.car_system.car_system_mock import CarSystemMock

class EAutomobileState(Enum):
    OCCUPIED = 0,
    AVAILABLE = 1,
    SUSPENDED = 2


class EVehicleState(Enum):
    ECONOM = 0,
    COMFORT = 1,
    BUSINESS = 2


class Automobile(object):
    def __init__(self):
        self.mark = None
        self.capacity = None
        self.car_system = CarSystemMock()
        self.vehicle_class = None
        self.auto_state = None
        self.automobile_coordinate = None

    def open_vehicle(self):
        result = self.car_system.check_systems()
        if not result:
            self.auto_state = EAutomobileState.SUSPENDED
            return result
        self.car_system.open_auto()
        return result

    def close_vehicle(self):
        pass

    def book(self):
        self.auto_state = EAutomobileState.OCCUPIED
