from .db import IDatabase
import json
from src.carsharing.user.user import User
import os
import pickle


class DataBaseMock(IDatabase):
    def __init__(self, config_file):
        print(os.getcwd())
        super().__init__(config_file)
        with open(config_file) as f:
            self.config = json.load(f)

        if os.path.exists(self.config["cars"]):
            with open(self.config["cars"], 'rb') as fin:
                self.cars = pickle.load(fin)
        else:
            self.cars = {}

        if os.path.exists(self.config["users"]):
            with open(self.config["users"], 'rb') as fin:
                self.users = pickle.load(fin)
        else:
            self.users = {}
        print(self.users)

        if os.path.exists(self.config["reviewers"]):
            with open(self.config["reviewers"], 'rb') as fin:
                self.reviewers = pickle.load(fin)
            print(self.reviewers)
        else:
            self.reviewers = {}

    def load_users(self):
        return User(self.users)

    def load_user(self, username):
        return self.users[username]

    def load_cars(self):
        return list(self.cars.values())

    def load_reviewers(self):
        return list(self.reviewers.values())

    def save_user(self, user):
        self.users[user.user_info.username] = user.user_info
        self.dump_database()

    def dump_database(self):
        with open(self.config["cars"], 'wb+') as fout:
            pickle.dump(self.cars, fout)

        with open(self.config["users"], 'wb+') as fout:
            pickle.dump(self.users, fout)

        with open(self.config["reviewers"], 'wb+') as fout:
            pickle.dump(self.reviewers, fout)
