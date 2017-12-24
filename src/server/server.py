import json
from collections import defaultdict

from ..external.db import DataBaseMock
from ..external.map_service.map_service import IMapService
from ..external.map_service.map_service_mock import MapServiceMock

from ..carsharing.user.user import EUserStatus, user_status_to_str, User
from ..carsharing.review.review_queue import ReviewQueue

from ..external.user_interaction import IUserInteraction, UserInteractionMock
from .configurator import Configurator


class Server(object):
    def __init__(self, args):
        # configure database
        self.database = DataBaseMock(args.dbconfig)
        Configurator.configure(self.database, args)
        self.review_queue = ReviewQueue.instance

        self.message_storage = defaultdict(list)
        IUserInteraction.get_by_user = lambda user: UserInteractionMock(self.message_storage[user.user_info.username])

        # configure map service
        IMapService.configure(MapServiceMock())

    def signup_user_handle(self, user_info):
        user = User(user_info)
        result = user.sign_up(self.review_queue)
        print(result)
        if result:
            user.user_interaction.receive_message(user_status_to_str(EUserStatus.NOT_APPROVED))
            # add user to db
            self.database.save_user(user)
        else:
            user.user_interaction.receive_message(user_status_to_str(EUserStatus.NOT_APPROVED))

    def check_account_handle(self, account):
        return account.username in self.database.users and self.database.users[account.username].password == account.password

    def get_messages_handle(self, username):
        if username in self.message_storage:
            return self.message_storage[username]

    def check_availible_autos_handle(self, username, coordinates):
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
