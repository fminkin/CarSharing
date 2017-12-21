class Zone(object):
    parking_zones = None
    ride_zones = None

    @staticmethod
    def configure_zones(parking_coords, ride_coords):
        Zone.parking_zones = Zone(parking_coords)
        Zone.ride_zones = Zone(ride_coords)

    def __init__(self, coordinates):
        self.coordinates = coordinates

    def contains(self, coordinate):
        # not implenting shit
        return True
