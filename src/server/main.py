import argparse
from ..contrib.db import DataBaseMock as DB
from ..carsharing.car_pool import CarPool
from ..carsharing.auto.automobile import EAutomobileState
from ..carsharing.review.review_queue import ReviewQueue
from ..carsharing.user.user import EUserStatus, user_status_to_str


class Server(object):
    def __init__(self, args):
        self.database = DB(args.dbconfig)
        self.users = self.database.load_users()
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
            self.users.append(user)
        else:
            user.user_interaction.receive_message(user_status_to_str(EUserStatus.NOT_APPROVED))

    def book_ride_action_handle(self, user, coordinates):
        user.check_available_autos(coordinates)




if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--dbconfig', type=str)

    server = Server(parser.parse_args())
