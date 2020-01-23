import configures


def search_in_dict(dicta):
    if type(dicta) == dict:
        for key, value in dicta.items():
            if key == configures.get_values_of_key:
                configures.list_values_of_key.append(value)
            else:
                search_in_dict(value)
    elif type(dicta) == list:

        for dicts in dicta:
            search_in_dict(dicts)


def rem_keys_not_cond(list_dicts):
    search_in_dict(list_dicts)

    return configures.list_values_of_key