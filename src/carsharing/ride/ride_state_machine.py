from enum import Enum
from .ride import Ride
from ..checkers.auto_state_checker import AutoStateChecker
from ..checkers.coords_checker import CoordsChecker
from src.contrib.map_service.map_service_mock import MapServiceMock

class ERideState(Enum):
    UNINITIALIZED = 0,
    RESERVED = 1,
    IN_PROGRESS = 2,
    SUCCESSFULLY_FINISHED = 3,
    TEMPORARY_ISSUE = 4,
    CRITICAL_ISSUE = 5


class ECheckerType(Enum):
    COORDS = 0,
    STATE = 1


class RideStateMachine(object):
    def __init__(self):
        self.ride = Ride()
        self.auto_state_checker = AutoStateChecker()
        self.coords_checker = CoordsChecker()
        self.ride_state = ERideState()
        self.map_service = MapServiceMock()
        self.car_pool = Car

    def checker_issue(self, checker_type):
        pass

    def no_issue(self, checker_type):
        pass

    def critical_issue(self):
        pass

    def check_availible_autos(self, coordinates):

        pass

    def vehicle_status_change_success(self):
        pass

    def start_ride(self, photos):
        pass

    def reserve_auto(self, automobile, charge_rate):
        pass

    def finish_ride(self):
        pass
