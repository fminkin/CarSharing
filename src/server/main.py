import argparse
from ..contrib.db import DataBaseMock as DB
from ..carsharing.car_pool import CarPool
from ..carsharing.auto.automobile import EAutomobileState
from ..carsharing.review.review_queue import ReviewQueue
from ..carsharing.user.user import EUserStatus, user_status_to_str
from cityhash import CityHash64


class Server(object):
    def __init__(self, args):
        self.database = DB(args.dbconfig)
        self.all_cars = self.database.load_cars()

        # load car_pool
        self.car_pool = CarPool()
        for car in self.all_cars:
            if car.auto_state == EAutomobileState.AVAILABLE:
                self.car_pool.push(car)

        self.reviewers = self.database.load_reviewers()
        self.review_queue = ReviewQueue(self.review_queue)

    def signup_user_handle(self, user):
        result = user.sign_up(self.review_queue)
        if result:
            user.user_interaction.receive_message(user_status_to_str(EUserStatus.NOT_APPROVED))
            # add user to db
            self.database.save_user(user)
        else:
            user.user_interaction.receive_message(user_status_to_str(EUserStatus.NOT_APPROVED))

    def book_ride_action_handle(self, user_info, coordinates):
        user = self.database.load_user(user_info)
        user.check_available_autos(coordinates)

    def reserve_auto_handle(self, user_info, automobile, charge_rate):
        user = self.database.load_user(user_info)
        user.reserve_auto(automobile, charge_rate)

    def start_ride_action_handle(self, user_info, photos):
        user = self.database.load_user(user_info)
        user.start_ride(photos)



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--dbconfig', type=str)

    server = Server(parser.parse_args())
