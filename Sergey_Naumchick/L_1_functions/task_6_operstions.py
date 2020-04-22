import configures


def search_in_dict(insights):
    if type(insights) == dict:
        for key, value in insights.items():
            if key == configures.key_for_unique:

                configures.list_unique_values.append(value)
            else:
                search_in_dict(value)
    elif type(insights) == list:

        for dicts in insights:
            search_in_dict(dicts)
    return list(set(configures.list_unique_values))
