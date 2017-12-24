from random import choice


class ReviewQueue():
    instance = None

    def __init__(self, reviewers):
        self.reviewers = reviewers

    @staticmethod
    def configure(reviewers):
        ReviewQueue.instance = ReviewQueue(reviewers)

    def submit(self, user):
        if self.reviewers:
            return choice(self.reviewers).review_documents(user.user_info.images)
        return False
