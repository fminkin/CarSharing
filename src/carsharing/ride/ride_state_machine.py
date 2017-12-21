from enum import Enum

from src.carsharing.checkers.checker_type import ECheckerType
from .ride import Ride
from ..checkers.auto_state_checker import AutoStateChecker
from ..checkers.coords_checker import CoordsChecker
from src.contrib.map_service.map_service import IMapService
from ..car_pool.car_pool import CarPool
from src.carsharing.utils.coordinate import TimedCoordinate
import time


class ERideState(Enum):
    UNINITIALIZED = 0,
    RESERVED = 1,
    IN_PROGRESS = 2,
    SUCCESSFULLY_FINISHED = 3,
    TEMPORARY_ISSUE = 4,
    CRITICAL_ISSUE = 5


class RideStateMachine(object):
    def __init__(self, user):
        self.ride = None
        self.auto_state_checker = None
        self.coords_checker = None
        self.ride_state = ERideState.UNINITIALIZED
        self.map_service = IMapService.instance
        self.car_pool = CarPool.instance
        self.user = user
        self.issue_start_times = {checker_type: None for checker_type in ECheckerType}
        self.max_issue_time = {ECheckerType.COORDS: 60, ECheckerType.STATE: 80}
        # may be parse it from config?

    def checker_issue(self, checker_type):
        if self.ride_state == ERideState.CRITICAL_ISSUE:
            return
        self.ride_state = ERideState.TEMPORARY_ISSUE

        self.user.user_interaction.receive_message("Temporary Issue")
        # change it to something meaningful
        if self.issue_start_times[checker_type] is None:
            self.issue_start_times[checker_type] = time.time()
            coordinates = self.map_service.get_closest_gas_stations(self.ride.coordinates[-1].coordinate)
            self.user.user_interaction.receive_nearest_gas_stations(coordinates)
        else:
            if time.time() - self.issue_start_times[checker_type] > self.max_issue_time[checker_type]:
                self.critical_issue()

    def no_issue(self, checker_type):
        if self.ride_state == ERideState.CRITICAL_ISSUE:
            return

        self.issue_start_times[checker_type] = None
        if not any(self.issue_start_times.values()):
            self.ride_state = ERideState.IN_PROGRESS

    def critical_issue(self):
        self.ride_state = ERideState.CRITICAL_ISSUE
        self.user.user_interaction.receive_message("Critical Issue")
        # change it to something meaningful

    def check_availible_autos(self, coordinates):
        automobiles = self.car_pool.get_automobiles_nearby(coordinates)
        return automobiles

    def vehicle_status_change_success(self):
        self.ride_state = ERideState.SUCCESSFULLY_FINISHED

    def start_ride(self, photos):
        assert (self.ride)
        self.ride.add_photos(photos)
        result = self.ride.automobile.open_vehicle()
        if result:
            self.ride_state = ERideState.IN_PROGRESS
        else:
            self.ride_state = ERideState.CRITICAL_ISSUE
            return result

        self.auto_state_checker = AutoStateChecker(self, self.ride.automobile.car_system)
        self.coords_checker = CoordsChecker(self, self.ride.automobile.car_system)
        self.ride.automobile.car_system.subscribe_on_coords_change(self)

        return result

    def reserve_auto(self, automobile, charge_rate, supply=False):
        if supply:
            self.car_pool.reserve_for_supply(automobile, self.user)
        else:
            if not self.car_pool.pop(automobile):
                return False
            automobile.book()
        self.ride = Ride(self.user, charge_rate, automobile)
        self.ride_state = ERideState.RESERVED
        return True

    def finish_ride(self):
        result = self.coords_checker.check_parking_zones(self.ride.coordinates[-1].coordinate)
        if result:
            self.user.user_interaction.receive_parking_zones(result)
            return
        closed = self.ride.automobile.close_vehicle()
        if not closed:
            self.ride_state = ERideState.CRITICAL_ISSUE
            self.user.user_interaction.receive_message("Fail")
            # may be refactor?
            return False
        self.ride.charge_user()
        self.car_pool.push(self.ride.automobile)


    def on_coordinate_change(self, coordinate):
        self.ride.add_coordinate(TimedCoordinate(coordinate))
