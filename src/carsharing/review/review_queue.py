from ..utils.singleton import Singleton


class ReviewQueue(metaclass=Singleton):
    def __init__(self, reviewers):
        self.reviewers = reviewers

    def submit(self, user):
        # we are not implementing this
        # cause the mechanism of choosing reviewer and
        # review itself is too complex
        return True

