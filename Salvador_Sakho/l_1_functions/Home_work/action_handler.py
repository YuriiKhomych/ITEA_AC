import Salvador_Sakho.l_1_functions.Home_work.dict_handler as dict_handler
import Salvador_Sakho.l_1_functions.Home_work.keys_handler as keys_handler
import Salvador_Sakho.l_1_functions.Home_work.globals_for_work as global_data
import Salvador_Sakho.l_1_functions.Home_work.set_handler as set_handler
import Salvador_Sakho.l_1_functions.Home_work.list_handler as list_handler
from Salvador_Sakho.l_1_functions.Home_work import type_handler

global_data.init()


def handle_action(collection, key=None, value=None, action=None):
    if action in ['remove_key', 'entities_to_list']:
        keys_handler.check_key(collection, key, action)
    elif action == 'to_dict':
        dict_handler.to_dict(key, value)
    elif action == 'to_list':
        list_handler.to_list([str(key), str(value)])
    elif action == 'to_set':
        set_handler.to_set(key, value)
    else:
        raise Exception(f'Unexpected type of action: {action}')


def run_process(list_comp, action=None):
    if type_handler.check_if_dict(list_comp):
        dict_handler.handle_dict_data(list_comp.values(), action=action)

    if type_handler.check_if_list(list_comp):
        list_handler.handle_list_data(list_comp, action=action)
