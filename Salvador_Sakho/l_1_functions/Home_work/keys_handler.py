import Salvador_Sakho.l_1_functions.Home_work.dict_handler as dict_handler
import Salvador_Sakho.l_1_functions.Home_work.type_handler as type_handler
import Salvador_Sakho.l_1_functions.Home_work.list_handler as list_handler
import Salvador_Sakho.l_1_functions.Home_work.globals_for_work as global_data

global_data.init()


def check_key(collection, key, action):
    if key in collection.keys():
        if ((key in global_data.keys_for_remove[1:7])
            or (key in [global_data.keys_for_remove[7][1],
                        global_data.keys_for_remove[8][1]]
                and collection[key] != 'EUR')) and action == 'remove_key':
            remove_by_key(collection, key)
        if key in [global_data.keys_for_remove[7][0],
                   global_data.keys_for_remove[8][
                       0]] and action == 'remove_key':
            if type_handler.check_if_dict(collection[key]):
                dict_handler.handle_dict_data(collection[key].values(),
                                              action=action)
            if type_handler.check_if_list(collection[key]):
                list_handler.handle_list_data(collection[key], action=action)
        if key == 'entities' and action == 'entities_to_list':
            entities_key_case_handler(collection)
    return collection


def remove_by_key(collection, key_val):
    with open('./keys_removed_log_file.txt', 'a+') as log_file:
        log_file.write(
            f'Removed key:{key_val}\n Collection{collection}\n******\n')
        if type_handler.check_if_dict(collection):
            if key_val in collection.keys():
                del collection[key_val]
        if type_handler.check_if_list(collection):
            collection.remove(key_val)
    return collection


def entities_key_case_handler(collection):
    for data in collection['entities']:
        if data['spend_sum'] > 200:
            global_data.entities_spend_sum.append(data)
