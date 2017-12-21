from ..utils.singleton import Singleton
from ..utils.coordinate import distance
from ..auto.automobile import AutomobileState

class CarPool(metaclass=Singleton):
    NEARBY_DISTANCE = 5

    def __init__(self):
        self.automobiles = {}

    def push(self, automobile):
        self.automobiles[automobile.id] = automobile

    def pop(self, automobile_id):
        del self.automobiles[automobile_id]

    def reserve_car(self, automobile_id):
        self.automobiles[automobile_id].auto_sate = AutomobileState.OCCUPIED

    def get_automobiles_nearby(self, coordinate):
        result = []
        for id, auto in self.automobiles.items():
            if distance(auto.automobile_coordinate, coordinate) < self.NEARBY_DISTANCE:
                result.append(auto)
        return result
