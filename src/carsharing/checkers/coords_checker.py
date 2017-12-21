from .checker import Checker
from ..utils.zone import Zone
from src.carsharing.ride.ride_state_machine import ECheckerType


class CoordsChecker(Checker):
    def __init__(self, ride_state_machine, car_system):
        super().__init__()
        self.ride_zones = Zone.ride_zones
        self.parking_zones = Zone.parking_zones
        # refactor this ???
        self.ride_state_machine = ride_state_machine
        self.car_system = car_system
        self.car_system.subscribe_on_coords_change(self)

    def on_coordinates_change(self, coordinate):
        if any([zone.contains(coordinate) for zone in self.ride_zones]):
            self.ride_state_machine.no_issue(ECheckerType.COORDS)
        else:
            self.ride_state_machine.checker_issue(ECheckerType.COORDS)

    def check_parking_zones(self, coordinate):
        if not any([zone.contains(coordinate) for zone in self.parking_zones]):
            return self.parking_zones
        return None


