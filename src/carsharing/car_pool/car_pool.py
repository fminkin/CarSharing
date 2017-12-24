from ..utils.coordinate import distance
from ..auto.automobile import EAutomobileState


class CarPool(object):
    NEARBY_DISTANCE = 5

    instance = None

    @staticmethod
    def configure(cars):
        print("CARS:", cars)
        CarPool.instance = CarPool()
        for car in cars:
            if car.auto_state == EAutomobileState.AVAILABLE:
                CarPool.instance.push(car)

    def __init__(self):
        self.automobiles = {}
        self.reserved = {}

    def push(self, automobile):
        print(automobile.license_plate)
        if automobile.license_plate in self.reserved:
            user = self.reserved[automobile.license_plate]
            user.user_interaction.receive_supplied()
            return
        automobile.auto_state = EAutomobileState.AVAILABLE
        self.automobiles[automobile.license_plate] = automobile
        print("SA", self.automobiles)

    def pop(self, automobile_plate):
        print(automobile_plate, self.automobiles)
        if automobile_plate in self.automobiles:
            del self.automobiles[automobile_plate]
            return True
        return False

    def reserve_for_supply(self, automobile, user):
        self.reserved[automobile.license_plate] = user

    def get_automobiles_nearby(self, coordinate):
        print(self.automobiles.items())
        result = []
        for _, auto in self.automobiles.items():
            if distance(auto.car_system.get_coordinate(), coordinate) <= self.NEARBY_DISTANCE:
                result.append(auto)
        return result
