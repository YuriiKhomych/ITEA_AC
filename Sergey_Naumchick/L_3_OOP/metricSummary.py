class MetricSummary():
    def __init__(self, metric_summary):
        self.metric_summary = metric_summary
        self.metrics = self.ms_sum(metric_summary)

    def __repr__(self):
        return str(self.__dict__)

    def __len__(self):

        return len(self.metrics)

    def ms_sum(self, metric_sum):
        result = []
        for key, value in metric_sum.items():
            result_1 = 0
            for val in value.values():

                if isinstance(val, (int, float)):
                    result_1 += (val)
            result.append(result_1)
            for i in result:
                if i > 6:
                    return sum(result)

        return result
