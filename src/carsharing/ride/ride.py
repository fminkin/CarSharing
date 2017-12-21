from enum import Enum


class EChargeRateType(Enum):
    MINUTELY = 0,
    DAILY = 1,
    CORPORATE = 2


class Ride(object):
    def __init__(self, user, charge_rate, automobile):
        self.charge_rate = charge_rate
        self.system_message = None
        self.photos = None
        self.user = user
        self.coordinates = None
        self.automobile = automobile

    def add_coordinate(self, coordinate):
        pass

    def add_photos(self, photos):
        pass

    def charge_user(self):
        pass
