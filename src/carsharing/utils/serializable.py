class Serializable(object):
    def serialize(self):
        raise NotImplementedError()

    @staticmethod
    def deserialize(serialization):
        raise NotImplementedError()
