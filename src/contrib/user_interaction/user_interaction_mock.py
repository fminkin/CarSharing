from .user_interaction import IUserInteraction


class UserInteractionMock(IUserInteraction):
    def __init__(self):
        super().__init__()
        pass

    def receive_message(self, message_text):
        pass

    def receive_nearest_gas_stations(self, gas_stations_coordinates):
        pass

    def receive_parking_zones(self, parking_zones):
        pass

    def receive_automobiles(self, automobiles):
        pass

    def want_supply(self, timed_coordinate):
        pass
