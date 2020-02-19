from meta_insight import MetaInsight
from MetricSummary import MetricSummary
from home_5 import time_laps


class BaseInsight(metaclass=MetaInsight):
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
        self.check_api(api)
        self.metric_name = metric_name
        self.report_name = report_name
        self.objective = objective
        self._unit = unit
        self._currency = currency
        self.id = id
        self.validator_insight_type = validator_insight_type
        self.metric_summary = metric_summary
        self.metrics = self.sums_of_metrics(metric_summary)



    @staticmethod
    # @time_laps
    def check_api(api):
        if api not in range(1, 5):
            raise KeyError(f"api {api} is out of range!")


    @staticmethod
    # @time_laps
    def sums_of_metrics(metric):
        return MetricSummary(metric)

    # @time_laps
    def __len__(self):
        return len(self.metrics)

    # Method that return report_name uppercase
    def method_report_name(self):
        return self.report_name.upper()


    # Get attribute value
    @time_laps
    def get_attribute_value(self, name):
        try:
            return getattr(self, name)
        except Exception as error:
            return error


    # Print attribute value
    @time_laps
    def get_attribute(self, name):
        print(self.get_attribute_value(name))


    @property
    def currency(self):
        return self._currency

    @property
    def unit(self):
        return self._unit

    @property
    def print(self):
        return 'print'

