

class IUserInteraction(object):
    def __init__(self):
        pass

    def receive_message(self, message_text):
        raise NotImplementedError("Pure virtual class")

    def receive_nearest_gas_stations(self, gas_stations_coordinates):
        raise NotImplementedError("Pure virtual class")

    def receive_automobiles(self, automobiles):
        raise NotImplementedError("Pure virtual class")

    def want_supply(self, timed_coordinate):
        raise NotImplementedError("Pure virtual class")

    @staticmethod
    def get_by_user(self, user):
        pass
