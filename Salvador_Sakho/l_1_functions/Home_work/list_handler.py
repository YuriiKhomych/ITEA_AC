import Salvador_Sakho.l_1_functions.Home_work.type_handler as type_handler
import Salvador_Sakho.l_1_functions.Home_work.dict_handler as dict_handler
import Salvador_Sakho.l_1_functions.Home_work.keys_handler as keys_handler
import Salvador_Sakho.l_1_functions.Home_work.globals_for_work as global_data
global_data.init()


def handle_list_data(list_data, key='', main_list=[], main_dict=dict(), action=''):
    for data in list_data:
        if type_handler.check_if_dict(data):
            dict_handler.handle_dict_data(data, main_list=global_data.main_list, main_dict=main_dict, action=action)
        elif type_handler.check_if_list(data):
            handle_list_data(data, main_list=global_data.main_list, main_dict=main_dict, action=action)
        elif type_handler.check_if_string(data) \
                or type_handler.check_if_boolean(data) \
                or type_handler.check_if_int(data) \
                or type_handler.check_if_float(data):
            if action == 'remove_key':
                list_data = keys_handler.check_and_remove(list_data, data)
            elif action == 'to_dict':
                global_data.general_id += 1
                main_dict[f'{global_data.general_id}'] = data
            elif action == 'to_list':
                main_list.append(str(data))
            elif action == 'campaign_id_collect':
                dict_handler.campaign_id_case_handler(data, key)
            elif action == 'to_set':
                global_data.main_set.add(data)
            else:
                raise Exception(f'Unexpected type of action: {action}')
        elif type_handler.check_if_none(data):
            pass
        else:
            raise Exception(f'Unexpected data type:{type(data)}')
