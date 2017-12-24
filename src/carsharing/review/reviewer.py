from ..utils.serializable import Serializable


class Reviewer(Serializable):
    def __init__(self):
        pass

    def serialize(self):
        pass

    @staticmethod
    def deserialize(serialization):
        return Reviewer()

    def review_documents(self, documents):
        return True
