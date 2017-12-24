from .user_interaction import IUserInteraction


class UserInteractionMock(IUserInteraction):
    def __init__(self, message_storage):
        super().__init__()
        self.message_storage = message_storage

    def receive_message(self, message_text):
        self._save_message("receive_message", message_text)

    def receive_nearest_gas_stations(self, gas_stations_coordinates):
        self._save_message("receive_nearest_gas_stations", gas_stations_coordinates)

    def receive_parking_zones(self, parking_zones):
        self._save_message("receive_parking_zones", parking_zones)

    def receive_automobiles(self, automobiles):
        self._save_message("receive_automobiles", automobiles)

    def want_supply(self, timed_coordinate):
        self._save_message("want_supply", timed_coordinate)

    def receive_supplied(self):
        self._save_message("receive_supplied", "")

    def _save_message(self, message, body):
        self.message_storage.append({"message": message, "body": body})
