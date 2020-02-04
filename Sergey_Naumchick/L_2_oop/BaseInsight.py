from metricSummary import MetricSummary


class BaseInsight:

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
        self.if_api(api)
        self.metric_name = metric_name
        self.api = api
        self.report_name = report_name
        self.objective = objective
        self.unit = unit
        self.currency = currency
        self.id = id
        self.validator_insight_type = validator_insight_type
        self.metrics = self.metr_s(metric_summary)

    def __eq__(self, other):
        if self.api == other.api:
            print("eq")

    @staticmethod
    def if_api(api):
        if api not in range(1, 5):
            raise KeyError("bad - api not in 1..4")

    @staticmethod
    def metr_s(metrics):
        my_dict = {}
        for key, value in metrics.items():
            my_dict[key] = MetricSummary(**value)
        return my_dict
