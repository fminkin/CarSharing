from enum import Enum


class UserStatus(Enum):
    NOT_APPROVED = 0,
    APPROVED = 1


class User(object):
    def __init__(self):
        pass

    def sign_up(self):
        pass

    def check_available_autos(self, coordinates):
        pass

    def reserve_auto(self, automobile, charge_rate):
        pass

    def finish_ride(self):
        pass

    def request_supply(self):
        pass

    def start_ride(self, photos):
        pass

    def change_balance(self, delta):
        pass
