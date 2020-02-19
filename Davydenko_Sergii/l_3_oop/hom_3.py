from hw_start import insights
from BaseInsight import BaseInsight
#
#
for insight in insights:
    try:
        bi = BaseInsight(**insight)

    except KeyError as err:
        print(f"Error: {err}")
    else:
        # print(f'{bi.get_attribute_value("metric_summary")}')
        # print('Print', bi.get_attribute('metric_summary'))
        # print(f'Report_name {bi.method_report_name()}')
        # print(f'Get api_name {bi.get_api_name()}')
        # print(f'Define Unit -  {bi.unit}')
        # print(f'Define currency - {bi.currency}')
        print(f'Define print - {bi.print}')
