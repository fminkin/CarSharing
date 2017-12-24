from .checker import Checker
from .checker_type import ECheckerType


class AutoStateChecker(Checker):
    def __init__(self, ride_state_machine, car_system):
        super().__init__(ride_state_machine)
        self.fuel_thr = 0.1
        self.liquid_thr = 0.1
        self.car_system = car_system
        self.car_system.subscribe_on_auto_state_change(self)

    def on_auto_state_change(self, state):
        if state.fuel < self.fuel_thr or state.liquid < self.liquid_thr:
            self.ride_state_machine.checker_issue(ECheckerType.STATE)
        else:
            self.ride_state_machine.no_issue(ECheckerType.STATE)
