import configures


# Task #2
def search_in_dict(dicta):
    if type(dicta) == dict:

        for key, value in dicta.items():
            if key == configures.name_label:
                search_in_dict_label(value)
            else:
                search_in_dict(value)
    elif type(dicta) == list:
        for dicts in dicta:
            search_in_dict(dicts)


def search_in_dict_label(dicta):
    if type(dicta) == dict:

        for key, value in dicta.items():

            if key == configures.search_key_n_eq:
                if value != configures.key_to_rem_not_cond:
                    configures.list_unit_not_eq.append(f"{key} - {value}")
            else:
                search_in_dict_label(value)
    elif type(dicta) == list:

        for dicts in dicta:
            search_in_dict_label(dicts)


def rem_keys_not_cond(list_dicts):
    search_in_dict(list_dicts)
    return len(configures.list_unit_not_eq)


"""
ПОИСК ПО ВСЕМУ ФАЙЛУ!!!

def search_in_dict(dicta):
    if type(dicta) == dict:
        for key, value in dicta.items():
            if key == configures.search_key_n_eq:
                if value != configures.key_to_rem_not_cond:
                    configures.list_unit_not_eq.append(f"{key} - {value}")
            else:
                search_in_dict(value)
    elif type(dicta) == list:

        for dicts in dicta:
            search_in_dict(dicts)


def rem_keys_not_cond(list_dicts):
    search_in_dict(list_dicts)

    return configures.list_unit_not_eq"""
