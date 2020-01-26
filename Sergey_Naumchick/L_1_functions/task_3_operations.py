import configures


def search_in_dict(insights):
    if isinstance(insights, dict):
        for key, value in insights.items():
            if key == configures.GET_VALUES_OF_KEY:
                configures.list_values_of_key.append(value)
            else:
                search_in_dict(value)
    elif isinstance(insights, list):
        for dicts in insights:
            search_in_dict(dicts)

    return configures.list_values_of_key
