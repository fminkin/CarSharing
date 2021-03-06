from .car_system import ICarSystem
from src.carsharing.utils.coordinate import Coordinate


class CarSystemMock(ICarSystem):
    def __init__(self):
        super().__init__()
        pass

    def check_systems(self):
        return True

    def open_auto(self):
        pass

    def close_auto(self):
        pass

    def subscribe_on_coords_change(self, subscriber):
        pass

    def subscribe_on_auto_state_change(self, subscriber):
        pass

    def get_coordinate(self):
        return Coordinate(1, 2)
