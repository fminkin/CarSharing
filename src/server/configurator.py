import json
from ..carsharing.car_pool import CarPool
from ..carsharing.review.review_queue import ReviewQueue
from ..carsharing.user.user_pool import UserPool
from ..carsharing.utils.zone import Zone


class Configurator:
    @staticmethod
    def configure(database, args):
        # configure CarPool
        CarPool.configure(database.load_cars())

        # configure ReviewQueue
        ReviewQueue.configure(database.load_reviewers())

        # configure zones
        with open(args.zones_config) as zones_config_file:
            parking_coords, ride_coords = json.load(zones_config_file)
            Zone.configure_zones(parking_coords, ride_coords)

        # configure user_pool
        UserPool.configure()
