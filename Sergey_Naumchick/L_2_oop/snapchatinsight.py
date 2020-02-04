from BaseInsight import BaseInsight


class SnapchatInsight(BaseInsight):
    def __init__(self, weight=None, type=None):
        self.weight = weight
        self.type = type
