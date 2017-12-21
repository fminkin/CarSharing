

class IMapService(object):

    instance = None

    @staticmethod
    def configure(instance):
        IMapService.instance = instance

    def __init__(self):
        pass

    def get_closest_gas_stations(self, coordinate):
        raise NotImplementedError("Pure virtual class")
