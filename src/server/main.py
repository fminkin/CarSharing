import argparse
import json

from ..contrib.db import DataBaseMock
from ..carsharing.car_pool import CarPool
from ..contrib.map_service.map_service import IMapService
from ..contrib.map_service.map_service_mock import MapServiceMock
from ..carsharing.review.review_queue import ReviewQueue
from ..carsharing.user.user import EUserStatus, user_status_to_str
from ..carsharing.user.user_pool import UserPool
from ..carsharing.utils.zone import Zone
from ..contrib.user_interaction import IUserInteraction, UserInteractionMock

class Server(object):
    def __init__(self, args):
        # configure database
        self.database = DataBaseMock(args.dbconfig)

        # configure CarPool
        CarPool.configure(self.database.load_cars())

        # configure ReviewQueue
        self.review_queue = ReviewQueue(self.database.load_reviewers())

        # configure zones
        with open(args.zones_config) as zones_config_file:
            parking_coords, ride_coords = json.load(zones_config_file)
            Zone.configure_zones(parking_coords, ride_coords)

        # configure user_pool
        UserPool.configure()

        # configure map service
        IMapService.configure(MapServiceMock())

        IUserInteraction.get_by_user = lambda user: UserInteractionMock(user.user_info.username,
                                                                        self.database)

    def signup_user_handle(self, user):
        result = user.sign_up(self.review_queue)
        if result:
            user.user_interaction.receive_message(user_status_to_str(EUserStatus.NOT_APPROVED))
            # add user to db
            self.database.save_user(user)
        else:
            user.user_interaction.receive_message(user_status_to_str(EUserStatus.NOT_APPROVED))

    def book_ride_action_handle(self, username, coordinates):
        user = self.database.load_user(username)
        user.check_available_autos(coordinates)

    def reserve_auto_handle(self, username, automobile, charge_rate):
        user = self.database.load_user(username)
        user.reserve_auto(automobile, charge_rate)

    def start_ride_action_handle(self, username, photos):
        user = self.database.load_user(username)
        user.start_ride(photos)

    def finish_ride_action_handle(self, username):
        user = self.database.load_user(username)
        user.finish_ride()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--dbconfig', type=str)
    parser.add_argument('--zones-config', dest='zones_config', type=str)

    server = Server(parser.parse_args())
