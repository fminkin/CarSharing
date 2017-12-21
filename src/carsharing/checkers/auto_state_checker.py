from .checker import Checker


class AutoStateChecker(Checker):
    def __init__(self):
        super().__init__()
        pass

    def on_auto_state_change(self, state):
        pass
