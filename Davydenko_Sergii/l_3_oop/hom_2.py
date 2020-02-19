from hw_start import insights
from BaseInsight import BaseInsight
# from MetricSummary import MetricSummary


for insight in insights:
    try:
        bi = BaseInsight(**insight)

    except KeyError as err:
        print(f"Error: {err}")
    else:
        # print(bi.__dict__)
        print(f'The metric is {bi.metrics.metrics}')
        print(f'The len of metrics is {len(bi)}')





