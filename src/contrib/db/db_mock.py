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

        if os.path.exists(self.config["reviewers"]):
            with open(self.config["reviewers"], 'rb') as fin:
                self.reviewers = pickle.load(fin)
        else:
            self.reviewers = {}

        if os.path.exists(self.config["messages"]):
            with open(self.config["messages"], 'rb') as fin:
                self.messages = pickle.load(fin)
        else:
            self.messages = {}

    def load_users(self):
        return self.users

    def load_user(self, username):
        return self.users[username]

    def load_cars(self):
        return list(self.cars.values())

    def load_reviewers(self):
        return list(self.reviewers.values())

    def save_user(self, user):
        self.users[user.user_info.username] = user
        self.dump_database()

    def save_message(self, username, message):
        if username not in self.messages:
            self.messages[username] = []
        self.messages[username].append(message)
        self.dump_database()

    def dump_database(self):
        with open(self.config["cars"], 'wb+') as fout:
            pickle.dump(self.cars, fout)

        #with open(self.config["users"], 'wb+') as fout:
        #    pickle.dump(self.users, fout)

        with open(self.config["reviewers"], 'wb+') as fout:
            pickle.dump(self.reviewers, fout)

        with open(self.config["messages"], 'wb+') as fout:
            pickle.dump(self.messages, fout)
