from enum import Enum


class ERideState(Enum):
    UNINITIALIZED = 0,
    RESERVED = 1,
    IN_PROGRESS = 2,
    SUCCESSFULLY_FINISHED = 3,
    TEMPORARY_ISSUE = 4,
    CRITICAL_ISSUE = 5


class ECheckerType(Enum):
    COORDS = 0,
    STATE = 1


class RideStateMachine(object):
    def __init__(self):
        pass

    def checker_issue(self, checker_type):
        pass

    def no_issue(self, checker_type):
        pass

    def critical_issue(self):
        pass

    def check_availible_autos(self, coordinates):

        pass

    def vehicle_status_change_success(self):
        pass

    def start_ride(self, photos):
        pass

    def reserve_auto(self, automobile, charge_rate):
        pass

    def finish_ride(self):
        pass
