from BaseInsight import BaseInsight


class Facebook(BaseInsight):
    def __init__(self, dimensions_dict, dimensions, **kwargs):
        self.dimensions_dict = dimensions_dict
        self.dimensions = dimensions
        super.__init__(**kwargs)
