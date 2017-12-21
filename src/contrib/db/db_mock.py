from .db import DataBase
import json
from cityhash import CityHash64
import os
import pickle


class DataBaseMock(DataBase):
    def __init__(self, config_file):
        super().__init__(config_file)
        with open(config_file) as f:
            self.config = json.load(f)

        if os.path.exists(self.config["users"]):
            with open(self.config["cars"]) as fin:
                self.users = pickle.load(fin)
        else:
            self.users = {}

        if os.path.exists(self.config["cars"]):
            with open(self.config["cars"]) as fin:
                self.cars = pickle.load(fin)
        else:
            self.cars = {}

        if os.path.exists(self.config["reviewers"]):
            with open(self.config["reviewers"]) as fin:
                self.reviewers = pickle.load(fin)
        else:
            self.reviewers = {}

    def load_users(self):
        return self.users

    def load_user(self, user_info):
        return self.users[CityHash64(user_info)]

    def load_cars(self):
        return list(self.cars.values())

    def load_reviewers(self):
        return list(self.reviewers.values())

    def save_user(self, user):
        self.users[CityHash64(user.user_info)] = user
        self.dump_database()

    def save_car(self, car):
        self.cars[CityHash64(car)] = car
        self.dump_database()

    def save_reviewer(self, reviewer):
        self.reviewers[CityHash64(reviewer)] = reviewer
        self.dump_database()

    def dump_database(self):
        with open(self.config["cars"]) as fout:
            pickle.dump(fout, self.cars)

        with open(self.config["users"]) as fout:
            pickle.dump(fout, self.cars)

        with open(self.config["reviewers"]) as fout:
            pickle.dump(fout, self.cars)
