from ..utils.coordinate import distance
from ..auto.automobile import EAutomobileState


class CarPool():
    NEARBY_DISTANCE = 5

    instance = None

    @staticmethod
    def configure(cars):
        CarPool.instance = CarPool()
        for car in cars:
            if car.auto_state == EAutomobileState.AVAILABLE:
                CarPool.instance.push(car)

    def __init__(self):
        self.automobiles = {}
        self.supply_plate_to_user = {}

    def push(self, automobile):
        if automobile.license_plate in self.supply_plate_to_user:
            user = self.supply_plate_to_user[automobile.license_plate]
            user.user_interaction.receive_supplied()
            return
        automobile.auto_state = EAutomobileState.AVAILABLE
        self.automobiles[automobile.license_plate] = automobile

    def pop(self, automobile_plate):
        if automobile_plate in self.automobiles:
            del self.automobiles[automobile_plate]
            return True
        return False

    def reserve_for_supply(self, automobile, user):
        self.supply_plate_to_user[automobile.license_plate] = user

    def get_automobiles_nearby(self, coordinate):
        result = []
        for _, auto in self.automobiles.items():
            if distance(auto.automobile_coordinate, coordinate) <= self.NEARBY_DISTANCE:
                result.append(auto)
        return result
