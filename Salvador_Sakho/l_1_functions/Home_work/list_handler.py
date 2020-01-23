import Salvador_Sakho.l_1_functions.Home_work.type_handler as type_handler
import Salvador_Sakho.l_1_functions.Home_work.dict_handler as dict_handler
import Salvador_Sakho.l_1_functions.Home_work.globals_for_work as global_data
import Salvador_Sakho.l_1_functions.Home_work.action_handler as action_handler
import Salvador_Sakho.l_1_functions.Home_work.keys_handler as keys_handler

global_data.init()


def handle_list_data(list_data, key=None, action=None, **collection):
    keys_handler.check_key(list_data, key)
    for data in list_data:
        if type_handler.check_if_dict(data):
            dict_handler.handle_dict_data(data, collection=collection, action=action)
        elif type_handler.check_if_list(data):
            handle_list_data(data, key=key, collection=collection, action=action)
        elif type_handler.check_if_string(data) \
                or type_handler.check_if_boolean(data) \
                or type_handler.check_if_int(data) \
                or type_handler.check_if_float(data):
            action_handler.handle_action(collection, key=key, value=data, action=action)


def to_list(*data):
    global_data.main_list.append(str(data[0]))


def objective_case_handler(list_comp):
    handle_list_data(list_comp, main_dict=global_data.main_dict, action='to_dict')
    return global_data.main_dict['objective']
