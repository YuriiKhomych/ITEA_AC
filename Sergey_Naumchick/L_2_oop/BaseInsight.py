from metricSummary import MetricSummary


class BaseInsight:

    def __init__(self,
                 metric_name,
                 api,
                 report_name,
                 objective,
                 unit,
                 currency,
                 id,
                 validator_insight_type,
                 metric_summary,
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
        # self.metrics = self.metr_s(metric_summary)
        # self.metr_s()

    @staticmethod
    def if_api(api):
        if api not in range(1, 4):
            raise KeyError("bad - api not in 1..4")

    # @staticmethod
    # def metr_s(metrics) -> dict:
    #     """
    #     Filter the values in metrics dict and replace it on MetricSummary instances
    #     :param metrics: List of dict where each element is some metric
    #     :type metrics: list
    #     :return: Dict of MetricSummary instances
    #     :rtype: dict
    #     """
    #
    #     if not isinstance(metrics, dict):
    #         return {}
    #
    #     metric_attributes = [attr for attr in dir(MetricSummary()) if not attr.startswith("__")
    #                          and not attr.endswith("__") and not attr.startswith("_")]
    #
    #     for key, params in metrics.items():
    #         metrics[key] = MetricSummary(**dict(filter(lambda param: param[0] in metric_attributes, params.items())))
    #
    #     return metrics
