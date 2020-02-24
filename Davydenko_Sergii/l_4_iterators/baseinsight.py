

class BaseInsight(dict):
    def __init__(self,
                 metric_name=None,
                 api=None,
                 report_name=None,
                 objective=None,
                 unit=None,
                 currency=None,
                 id=None,
                 validator_insight_type=None,
                 metric_summary=None,
                 **kwargs,
                 ):
        self.api = api
        self.metric_name = metric_name
        self.report_name = report_name
        self.objective = objective
        self._unit = unit
        self._currency = currency
        self.id = id
        self.validator_insight_type = validator_insight_type
        self.metric_summary = metric_summary
        self.metrics = self.metric_summary


    def to_dict(self):
        return self.__dict__

    @classmethod
    def from_dict(cls, insights):
        return cls(**insights)

    def get_item(self, key):
        return self.metrics[key]

    def set_item(self, key, value):
        self.metrics[key] = value

    def del_item(self, key):
        del self.metrics[key]









    # try:
    #     def __delitem__(self, key):
    #         value = super().pop(key)
    #         super().pop(value, None)
    # except Exception as error:
    #     print(f'{error}')
    #
    #
    # def __setitem__(self, key, value):
    #     if key in self:
    #         del self[self[key]]
    #     if value in self:
    #         del self[value]
    #     super().__setitem__(key, value)


