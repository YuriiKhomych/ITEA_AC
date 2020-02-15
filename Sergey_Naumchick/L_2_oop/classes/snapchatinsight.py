from BaseInsight import BaseInsight


class SnapchatInsight(BaseInsight):
    def __init__(self, weight=None, type=None, **kwargs):
        self.weight = weight
        self.type = type
        super.__init__(**kwargs)
