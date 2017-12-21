from .user_interaction import IUserInteraction


class UserInteractionMock(IUserInteraction):
    def __init__(self, username, database):
        super().__init__()
        self.username = username
        self.database = database

    def receive_message(self, message_text):
        self._save_message_to_db("receive_message", message_text)

    def receive_nearest_gas_stations(self, gas_stations_coordinates):
        self._save_message_to_db("receive_nearest_gas_stations", gas_stations_coordinates)

    def receive_parking_zones(self, parking_zones):
        self._save_message_to_db("receive_parking_zones", parking_zones)

    def receive_automobiles(self, automobiles):
        self._save_message_to_db("receive_automobiles", automobiles)

    def want_supply(self, timed_coordinate):
        self._save_message_to_db("want_supply", timed_coordinate)

    def receive_supplied(self):
        self._save_message_to_db("receive_supplied", "")

    def _save_message_to_db(self, message, body):
        self.database.save_message(self.username, {"message": message, "body": body})
