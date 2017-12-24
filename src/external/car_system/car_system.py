

class ICarSystem(object):
    def __init__(self):
        pass

    def check_systems(self):
        raise NotImplementedError("Pure virtual class")

    def open_auto(self):
        raise NotImplementedError("Pure virtual class")

    def close_auto(self):
        raise NotImplementedError("Pure virtual class")

    def subscribe_on_coords_change(self, subscriber):
        raise NotImplementedError("Pure virtual class")

    def subscribe_on_auto_state_change(self, subscriber):
        raise NotImplementedError("Pure virtual class")

    def get_coordinate(self):
        raise NotImplementedError()
