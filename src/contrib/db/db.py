

class DataBase(object):
    def __init__(self, config_file):
        pass

    def load_users(self):
        raise NotImplementedError("Pure virtual class")

    def load_cars(self):
        raise NotImplementedError("Pure virtual class")

    def load_reviewers(self):
        raise NotImplementedError("Pure virtual class")

    def load_user(self, user_info):
        raise NotImplementedError("Pure virtual class")

    def save_user(self, user):
        raise NotImplementedError("Pure virtual class")

    def save_car(self, car):
        raise NotImplementedError("Pure virtual class")

    def save_reviewer(self, reviewer):
        raise NotImplementedError("Pure virtual class")