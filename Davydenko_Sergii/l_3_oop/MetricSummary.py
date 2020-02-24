class MetricSummary:
    def __init__(self, metric_summary):
        self.metric_summary = metric_summary
        self.metrics = self.sums_of_metrics(metric_summary)

    def __repr__(self):
        return str(self.__dict__)

    def __len__(self):
        return len(self.metrics)

    def sums_of_metrics(self, metric_summary):
        result = []

        for key, value in metric_summary.items():
            result_sum = 0
            for val in value.values():
                if isinstance(val, (int, float)):
                    result_sum += val
            result.append(result_sum)
            # for i in result:
            #     if i > 30:
            #         return sum(result)

        return result
