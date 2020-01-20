import Salvador_Sakho.l_1_functions.Home_work.dict_handler as dict_handler
import Salvador_Sakho.l_1_functions.Home_work.type_handler as type_handler
import Salvador_Sakho.l_1_functions.Home_work.list_handler as list_handler


def remove_keys(collection, keys):
    global REMOVE_KEYS
    REMOVE_KEYS = keys
    if type_handler.check_if_dict(collection):
        dict_handler.handle_dict_data(collection, action='remove_key')
    if type_handler.check_if_list(collection):
        list_handler.handle_list_data(collection, action='remove_key')


def check_and_remove(collection, key_val):
    if (key_val in REMOVE_KEYS[1:7]) \
            or (key_val in [REMOVE_KEYS[7][1], REMOVE_KEYS[8][1]] and collection[key_val] != 'EUR'):
        with open('./keys_removed_log_file.txt', 'a+') as log_file:
            log_file.write(f'Removed key:{key_val}\n Collection{collection}\n******\n')
            if type_handler.check_if_dict(collection):
                del collection[key_val]
            if type_handler.check_if_list(collection):
                collection.remove(key_val)
    if key_val in [REMOVE_KEYS[7][0], REMOVE_KEYS[8][0]]:
        if type_handler.check_if_dict(collection[key_val]):
            dict_handler.handle_dict_data(collection[key_val].values())
        if type_handler.check_if_list(collection[key_val]):
            list_handler.handle_list_data(collection[key_val])
    return collection
