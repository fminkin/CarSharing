from enum import Enum
from ..review.review_queue import ReviewQueue
from ..ride.ride_state_machine import RideStateMachine
from src.contrib.user_interaction.user_interaction_mock import UserInteractionMock


class EUserStatus(Enum):
    NOT_APPROVED = 0,
    APPROVED = 1


def user_status_to_str(user_status):
    if user_status.NOT_APPROVED:
        return "We are sorry, but You have note been approved!"
    else: # approved
        return "Congratulations, You have been approved!"


class User(object):
    def __init__(self):
        self.ride_state_machine = None
        self.user_interaction = UserInteractionMock()

    def sign_up(self, review_queue):
        return review_queue.submit(self)

    def check_available_autos(self, coordinates):
        self.ride_state_machine = RideStateMachine()
        self.ride_state_machine.check_availible_autos()

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
