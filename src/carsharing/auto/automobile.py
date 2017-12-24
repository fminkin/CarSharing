from enum import Enum
from src.external.car_system.car_system_mock import CarSystemMock
from ..utils.serializable import Serializable


class EAutomobileState(Enum):
    OCCUPIED = 0,
    AVAILABLE = 1,
    SUSPENDED = 2


class EVehicleClass(Enum):
    ECONOM = 0,
    COMFORT = 1,
    BUSINESS = 2


class Automobile(Serializable):
    def __init__(self, mark, capacity, license_plate, vehicle_class):
        self.mark = mark
        self.capacity = capacity
        self.license_plate = license_plate
        self.car_system = CarSystemMock()
        self.vehicle_class = vehicle_class
        self.auto_state = EAutomobileState.AVAILABLE

    def serialize(self):
        return [self.mark, self.capacity, self.license_plate, self.vehicle_class]

    @staticmethod
    def deserialize(serialization):
        return Automobile(*serialization)

    def open_vehicle(self):
        result = self.car_system.check_systems()
        if not result:
            self.auto_state = EAutomobileState.SUSPENDED
            return result
        self.car_system.open_auto()
        return result

    def close_vehicle(self):
        result = self.car_system.check_systems()
        if not result:
            self.auto_state = EAutomobileState.SUSPENDED
            return result
        self.car_system.close_auto()
        return result

    def book(self):
        self.auto_state = EAutomobileState.OCCUPIED
