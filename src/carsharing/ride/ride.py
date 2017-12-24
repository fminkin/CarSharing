from enum import Enum


class EChargeRateType(Enum):
    MINUTELY = 0,
    DAILY = 1,
    CORPORATE = 2


def get_charge_rate(num):
    if num == 0:
        return EChargeRateType.MINUTELY
    if num == 1:
        return EChargeRateType.DAILY
    if num == 2:
        return EChargeRateType.CORPORATE


class Ride(object):
    def __init__(self, user, charge_rate, automobile):
        self.charge_rate = charge_rate
        self.photos = []
        self.user = user
        self.coordinates = []
        self.automobile = automobile

    def add_coordinate(self, coordinate):
        self.coordinates.append(coordinate)

    def add_photos(self, photos):
        for photo in photos:
            self.photos.append(photo)

    def _calculate_charge_value(self):
        return len(self.coordinates) * (self.charge_rate.value[0] + 1)

    def charge_user(self):
        self.user.change_balance(-self._calculate_charge_value())
