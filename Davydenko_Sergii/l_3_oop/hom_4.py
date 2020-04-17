from hw_start import insights
from BaseInsight import BaseInsight

for insight in insights:
    try:
        bi = BaseInsight(**insight)

    except Exception as error:
        print(error)

    else:
        print(bi.sums_of_metrics)
        print(bi.method_report_name)
        print(bi.get_attribute_value)
        print(bi.__dict__)
