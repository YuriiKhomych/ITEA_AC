from BaseInsight import BaseInsight


class TwitterInsights(BaseInsight):
    def __init__(self, first_data=None, last_date=None, **kwargs):
        self.first_data = first_data
        self.last_date = last_date
        super.__init__(**kwargs)
