import configures


def search_in_dict(dicta):
    if type(dicta) == dict:
        for key, value in dicta.items():
            if key == configures.key_for_unique:


                configures.list_unique_values.append(value)
            else:
                search_in_dict(value)
    elif type(dicta) == list:

        for dicts in dicta:
            search_in_dict(dicts)


def get_unique(list_dicts):
    search_in_dict(list_dicts)

    return list(set(configures.list_unique_values))