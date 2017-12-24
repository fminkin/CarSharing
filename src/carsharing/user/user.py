from enum import Enum

from ..ride.ride_state_machine import RideStateMachine
from src.external.user_interaction import IUserInteraction
from ..user.user_pool import UserPool


class EUserStatus(Enum):
    NOT_APPROVED = 0
    APPROVED = 1


def user_status_to_str(user_status):
    if user_status == EUserStatus.NOT_APPROVED:
        return "We are sorry, but You have note been approved!"
    else: # approved
        return "Congratulations, You have been approved!"


class User(object):
    def __init__(self, user_info):
        self.ride_state_machine = None
        self.user_info = user_info
        self.user_pool = UserPool.instance
        self.balance = 0.0
        self.user_interaction = IUserInteraction.get_by_user(self)

    def sign_up(self, review_queue):
        return review_queue.submit(self)

    def check_available_autos(self, coordinates):
        self.ride_state_machine = RideStateMachine(self)
        result = self.ride_state_machine.check_availible_autos(coordinates)
        if not result:
            self.user_interaction.receive_message("Fail")
            # refactor this
            return
        self.user_interaction.receive_automobiles(result)

    def reserve_auto(self, automobile, charge_rate):
        result = self.ride_state_machine.reserve_auto(automobile, charge_rate)
        if not result:
            self.user_interaction.receive_message("Fail")
            # refactor this
            return
        self.user_interaction.receive_message("OK")
        # refactor this

    def finish_ride(self):
        self.ride_state_machine.finish_ride()
        self.ride_state_machine = None

    def request_supply(self, coords, charge_rate):
        supplier = self.user_pool.get_supplier(coords)
        if supplier is None:
            self.user_interaction.receive_message("Sorry no suppliers")
            return
        supplier.change_balance(5)
        self.change_balance(-5)
        automobile = supplier.ride_state_machine.ride.automobile
        self.ride_state_machine = RideStateMachine(self)
        self.ride_state_machine.reserve_auto(automobile, charge_rate, supply=True)

    def start_ride(self, photos):
        result = self.ride_state_machine.start_ride(photos)
        if not result:
            self.user_interaction.receive_message("Fail")
            # refactor this
            return
        self.user_interaction.receive_message("OK")

    def change_balance(self, delta):
        self.balance += delta
