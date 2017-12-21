class UserPool():
    instance = None

    @staticmethod
    def configure():
        UserPool.instance = UserPool()

    def __init__(self):
        self.users = {}

    def push(self, user):
        self.users[user.user_info.username] = user

    def pop(self, username):
        del self.users[username]

    def get_supplier(self, timed_coords):
        for user in self.users.values():
            if user.user_interaction.want_supply(timed_coords):
                user.change_balance(5)
                return user
