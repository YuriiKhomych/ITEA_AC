import configures


# Task #1 (A)
def removing(
        key,
        new_dict,
        list_to_rem=configures.keys_to_rem_root_lvl,

):
    if key in list_to_rem:
        configures.list_deleted_1_a.append(f"{key}")
        del new_dict[key]


def remove_unused_keys(list_dicts):
    for dicts in list_dicts:
        n_dict = dicts.copy()

        for key, value in dicts.items():
            removing(key, n_dict)

    return configures.list_deleted_1_a


# Task #1 (B)
def rem_ent_aff(list_dicts):
    for dicts in list_dicts:

        for key, value in dicts.items():
            if key == "entities_affected":

                for key_ent_eff, values_ent_eff in value.items():
                    if key_ent_eff == "entities":

                        for dicts_in_list_ent in values_ent_eff:
                            n_dict = dicts_in_list_ent.copy()

                            for key_dict_fin, val_dict_fin in dicts_in_list_ent.items():

                                if key_dict_fin in configures.key_to_rem_ent_affec:
                                    configures.list_deleted_1_b.append(f"{key_dict_fin}")
                                    del n_dict[key_dict_fin]

    return configures.list_deleted_1_b
