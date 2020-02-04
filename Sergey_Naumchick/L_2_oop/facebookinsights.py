import BaseInsight


class FacebookInsight(BaseInsight.BaseInsight):
    def __init__(self, dimensions_dict=None, dimensions=None,**kwargs):
        self.dimensions_dict = dimensions_dict
        self.dimensions = dimensions


        super().__init__(**kwargs)


