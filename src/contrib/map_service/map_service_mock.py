from .map_service import IMapService


class MapServiceMock(IMapService):
    def __init__(self):
        super().__init__()
        pass

    def get_closest_gas_stations(self):
        pass
