from .car_system import ICarSystem


class CarSystemMock(ICarSystem):
    def __init__(self):
        super().__init__()
        pass

    def check_systems(self):
        pass

    def open_auto(self):
        pass

    def close_auto(self):
        pass

    def subscribe_on_coords_change(self, subscriber):
        pass

    def subscribe_on_auto_state_change(self, subscriber):
        pass
