from BaseInsight import BaseInsight


class GoogleInsights(BaseInsight):
    def __init__(self, actions, **kwargs):
        self.actions = actions
        super.__init__(**kwargs)
