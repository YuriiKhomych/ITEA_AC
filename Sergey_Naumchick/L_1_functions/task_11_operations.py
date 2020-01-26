def chenge_period(insights):
    if isinstance(insights, dict):
        for key, value in insights.items():
            if key == "period" and value is None:
                insights[key] = 7
            elif key == "period" and value > 4:
                insights[key] = 7

            if key == "metric_sums":
                for dicts in value:
                    dict_formula = {
                        1: lambda: (dicts["sum"] * dicts["sum_level"] / dicts["sum_general"]) / insights["period"],
                        2: lambda: (dicts["sum"] * dicts["sum_level"] ** 2 / dicts["sum_general"]) / insights["period"],
                        3: lambda: (dicts["sum_level"] / dicts["sum_general"]) / insights["period"],
                        4: lambda: (dicts["sum_level"] * 100) / insights["period"]}
                    if dicts["sum_general"] != 0:
                        if insights["api"] == 1:
                            dicts["summary"] = dict_formula[1]
                    if insights["api"] == 2:
                        dicts["summary"] = dict_formula[2]
                    if insights["api"] == 3:
                        dicts["summary"] = dict_formula[3]
                    if insights["api"] == 4:
                        dicts["summary"] = dict_formula[4]
                    else:
                        dicts["summary"] = "Zero division problem!"

    if isinstance(insights, list):
        for dicts in insights:
            chenge_period(dicts)


def calc_summary(insights):
    chenge_period(insights)

    return insights
