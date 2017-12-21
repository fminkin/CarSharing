from enum import Enum
from ..review.review_queue import ReviewQueue
from ..ride.ride_state_machine import RideStateMachine

class UserStatus(Enum):
    NOT_APPROVED = 0,
    APPROVED = 1


class User(object):
    def __init__(self):
        self.ride_state_machine = None

    def sign_up(self):
        ReviewQueue().submit(self)

    def check_available_autos(self, coordinates):
        self.ride_state_machine = RideStateMachine()
        self.ride_state_machine.


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
