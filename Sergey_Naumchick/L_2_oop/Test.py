import copy


def insight_builder(insights):
    m_keys = ("metric_name",
              "api",
              "report_name",
              "objective",
              "unit",
              "currency",
              "id",
              "validator_insight_type",
              )
    all_keys = {}
    copy_insight = []

    if isinstance(insights, dict):
        for key, value in insights.items():
            if key in m_keys:
                all_keys[key] = value
                copy_insight = copy.deepcopy(all_keys)
        return print(copy_insight)

    elif isinstance(insights, list):
        for insight in insights:
            insight_builder(insight)
