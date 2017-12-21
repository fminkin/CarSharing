from .map_service import IMapService
from src.carsharing.utils.coordinate import Coordinate


class MapServiceMock(IMapService):
    def __init__(self):
        super().__init__()
        pass

    def get_closest_gas_stations(self, coordinate):
        # the closest ones
        return [Coordinate(1, 2), Coordinate(98, 42), Coordinate(42, 42)]
