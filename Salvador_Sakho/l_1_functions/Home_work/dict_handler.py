import Salvador_Sakho.l_1_functions.Home_work.type_handler as type_handler
import Salvador_Sakho.l_1_functions.Home_work.list_handler as list_handler
import Salvador_Sakho.l_1_functions.Home_work.keys_handler as keys_handler
import Salvador_Sakho.l_1_functions.Home_work.globals_for_work as global_data
from copy import copy

global_data.init()


def handle_dict_data(dictionary, main_list=[], main_dict=[str, str], action=None):
    temp_dict = copy(dictionary)
    for key, val in temp_dict.items():
        if type_handler.check_if_dict(val):
            handle_dict_data(val, main_list=main_list, main_dict=main_dict, action=action)
        elif type_handler.check_if_list(val):
            list_handler.handle_list_data(val, key=key, main_list=main_list, main_dict=main_dict, action=action)
        elif type_handler.check_if_string(val) \
                or type_handler.check_if_boolean(val) \
                or type_handler.check_if_int(val) \
                or type_handler.check_if_float(val):
            if action == 'remove_key':
                dictionary = keys_handler.check_and_remove(dictionary, key)
            elif action == 'to_dict':
                if key in main_dict.keys():
                    global_data.general_id += 1
                    main_dict[f'{key}_{global_data.general_id}'] = val
                elif action == 'calculate_metric_sums':
                    metric_sums_case_handler(key)
                else:
                    main_dict[key] = val
            elif action == 'to_list':
                main_list.append([str(key), str(val)])
            elif action == 'campaign_id_collect':
                campaign_id_case_handler(val, key)
            elif action == 'to_set':
                global_data.main_set.add((key, val))
            else:
                raise Exception(f'Unexpected type of action: {action}')
        elif type_handler.check_if_none(val):
            pass
        else:
            raise Exception(f'Unexpected data type:{type(val)}')


def campaign_id_case_handler(val, key=''):
    if key == 'campaign_id':
        if type_handler.check_if_dict(val):
            handle_dict_data(val, action='campaign_id_collect')
        elif type_handler.check_if_list(val):
            list_handler.handle_list_data(val, action='campaign_id_collect')
        else:
            global_data.campaign_id_dict['campaign_id'].append(val)


def metric_sums_case_handler():
    sum_total = 0
    sum_level_total = 0
    sum_general = 0
    for k, v in global_data.main_dict.items():
        if 'sum' in k:
            sum_total += float(v or 0)
        if 'sum_level' in k:
            sum_level_total += float(v or 0)
        if 'sum_general' in k:
            sum_general += float(v or 0)
    return sum_total, sum_level_total, sum_general
