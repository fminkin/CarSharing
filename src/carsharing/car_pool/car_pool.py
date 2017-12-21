from ..utils.singleton import Singleton
from ..utils.coordinate import distance
from ..auto.automobile import EAutomobileState


class CarPool(metaclass=Singleton):
    NEARBY_DISTANCE = 5

    def __init__(self):
        self.automobiles = {}

    def push(self, automobile):
        automobile.auto_state = EAutomobileState.AVAILABLE
        self.automobiles[automobile.license_plate] = automobile

    def pop(self, automobile_plate):
        del self.automobiles[automobile_plate]

    def reserve_car(self, automobile_plate):
        self.automobiles[automobile_plate].auto_sate = EAutomobileState.OCCUPIED

    def get_automobiles_nearby(self, coordinate):
        result = []
        for _, auto in self.automobiles.items():
            if distance(auto.automobile_coordinate, coordinate) <= self.NEARBY_DISTANCE:
                result.append(auto)
        return result
