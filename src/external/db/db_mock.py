from .db import IDatabase
import json
from src.carsharing.user.user import User
from src.carsharing.auto.automobile import Automobile
from src.carsharing.review.reviewer import Reviewer

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
                self.cars = [Automobile.deserialize(auto) for auto in pickle.load(fin)]
        else:
            self.cars = []
        print(self.cars)

        if os.path.exists(self.config["users"]):
            with open(self.config["users"], 'rb') as fin:
                self.users = [User.deserialize(user) for user in pickle.load(fin)]
        else:
            self.users = []
        print(self.users)
        for user in self.users:
            print(user.user_info.username, user.user_interaction)

        if os.path.exists(self.config["reviewers"]):
            with open(self.config["reviewers"], 'rb') as fin:
                self.reviewers = [Reviewer.deserialize(reviewer) for reviewer in pickle.load(fin)]
        else:
            self.reviewers = []
        print(self.reviewers)

    def load_users(self):
        return self.users

    def load_user(self, username):
        for user in self.users:
            if user.user_info.username == username:
                return user
        return None

    def load_cars(self):
        return self.cars

    def load_car(self, license_plate):
        for car in self.cars:
            if car.license_plate == license_plate:
                return car
        return None

    def load_reviewers(self):
        return self.reviewers

    def save_user(self, user):
        for i in range(len(self.users)):
            if self.users[i].user_info.username == user.user_info.username:
                self.users[i] = user
                break
        else:
            self.users.append(user)
        self.dump_database()

    def dump_database(self):
        with open(self.config["cars"], 'wb+') as fout:
            pickle.dump([car.serialize() for car in self.cars], fout)

        with open(self.config["users"], 'wb+') as fout:
            pickle.dump([user.serialize() for user in self.users], fout)

        with open(self.config["reviewers"], 'wb+') as fout:
            pickle.dump([reviewer.serialize() for reviewer in self.reviewers], fout)
