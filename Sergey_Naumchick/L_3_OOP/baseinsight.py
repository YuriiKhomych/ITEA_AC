import task_1
import metricSummary
from dec_func_time import benchmark


class BaseInsight:
    def __init__(self,
                 metric_name=None,
                 api=None,
                 report_name=None,
                 objective=None,
                 unit=None,
                 currency=None,
                 validator_insight_type=None,
                 metric_summary=None,

                 **kwargs):
        self.api = api
        self.check_api(api)

        self.period = task_1.set_period(api)
        self.metric_name = metric_name
        self.report_name = self.return_rep_ame(report_name)
        self.objective = objective
        self.unit = unit
        self.currency = currency
        self.validator_insight_type = validator_insight_type
        self.metric_summary = metric_summary
        self.metrics = self.metr_s(metric_summary)
        self.printing_res = self.print_val(currency, unit)
        print(task_1.collect_val_network(api))

    def __len__(self):
        return len(self.metrics)

    # Define property for currency, unit, and print value.
    @staticmethod
    def print_val(currency, unit):
        return currency, unit

    # Checking if api is in range 1..4
    @staticmethod
    @benchmark
    def check_api(api):
        if api not in range(1, 5):
            raise KeyError(f"api {api} is out of range!")

    # Getting attribute by name
    def get_attribute_by_name(self, name):
        try:
            return getattr(self, name)
        except Exception:
            print("no such name!")

    # Getting metrics
    @staticmethod
    def metr_s(metrics):
        return metricSummary.MetricSummary(metrics)

    # Returning report_name meaning UPPERCASE
    @staticmethod
    def return_rep_ame(rep_name):
        return rep_name.upper()
