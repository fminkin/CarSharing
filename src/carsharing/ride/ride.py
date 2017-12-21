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
        self.coordinates.append(coordinate)

    def add_photos(self, photos):
        self.photos = photos

    def _calculate_charge_value(self):
        return len(self.coordinates) * (self.charge_rate.value + 1)

    def charge_user(self):
        self.user.change_balance(-self._calculate_charge_value())
