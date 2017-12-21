from enum import Enum
from .ride import Ride
from ..checkers.auto_state_checker import AutoStateChecker
from ..checkers.coords_checker import CoordsChecker
from src.contrib.map_service.map_service_mock import MapServiceMock
from ..car_pool.car_pool import CarPool

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
    def __init__(self, user):
        self.ride = None
        self.auto_state_checker = AutoStateChecker()
        self.coords_checker = CoordsChecker()
        self.ride_state = ERideState()
        self.map_service = MapServiceMock()
        self.car_pool = CarPool()
        self.user = user

    def checker_issue(self, checker_type):
        pass

    def no_issue(self, checker_type):
        pass

    def critical_issue(self):
        pass

    def check_availible_autos(self, coordinates):
        automobiles = self.car_pool.get_automobiles_nearby(coordinates)
        return automobiles

    def vehicle_status_change_success(self):
        pass

    def start_ride(self, photos):
        pass

    def reserve_auto(self, automobile, charge_rate):

        result = self.car_pool.reserve_car(automobile)
        if not result:
            return False

        automobile.book()
        self.ride = Ride(self.user, charge_rate, automobile)
        # refactor this may be pass args to constructor
        return True


    def finish_ride(self):
        pass
