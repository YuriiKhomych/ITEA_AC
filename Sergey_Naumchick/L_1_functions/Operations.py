from hw_start import insights
import Main


def removing(
        key,
        new_dict,
        value=None,
        list_to_rem=Main.list_keys_to_del,
        list_deleted=Main.list_deleted,
):
    if key in list_to_rem:
        Main.list_deleted.append(f"{key}")
        del new_dict[key]


def remove_unused_keys(list_dicts):
    for dicts in list_dicts:
        n_dict = dicts.copy()

        for key, value in dicts.items():
            removing(key, n_dict, value)

            if type(value) == list:
                for val_list in value:
                    try:
                        for key_1, val_1 in val_list.items():
                            removing(key_1, n_dict, val_1)
                    except Exception:
                        pass
            if type(value) == dict:
                try:

                    for key_2, val_2 in value.items():
                        removing(key_2, n_dict, val_2)
                except Exception:
                    pass
            try:

                for dicts_in_val in value:
                    if type(dicts_in_val) == dict:

                        for keys, values in dicts_in_val.items():
                            removing(keys, values, dicts_in_val)


            except Exception:
                pass
    return Main.list_deleted


print(len(remove_unused_keys(insights)))

# лист диктов лежит в листе листов которые являются значением одного из диктов в списке диктов
