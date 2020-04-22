def search_in_dict(insights):
    if isinstance(insights, dict):
        for key, value in insights.items():
            if key == "report_name" and value == "device":
                insights[key] = value.upper()
            else:
                search_in_dict(value)
    elif isinstance(insights, list):
        for dicts in insights:
            search_in_dict(dicts)
    return insights
