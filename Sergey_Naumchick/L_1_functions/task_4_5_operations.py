import configures


def search_in_dict(insights):
    if type(insights) == dict:
        for key, value in insights.items():
            if key == configures.get_values_of_key_d:

                configures.dict_values_of_key[key] = value
                configures.list_values_of_key_d.append(configures.dict_values_of_key)
            else:
                search_in_dict(value)
    elif type(insights) == list:

        for dicts in insights:
            search_in_dict(dicts)
    return configures.list_values_of_key_d
