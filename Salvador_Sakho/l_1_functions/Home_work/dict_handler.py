from functools import reduce

import Salvador_Sakho.l_1_functions.Home_work.action_handler as action_handler
import Salvador_Sakho.l_1_functions.Home_work.type_handler as type_handler
import Salvador_Sakho.l_1_functions.Home_work.list_handler as list_handler
import Salvador_Sakho.l_1_functions.Home_work.globals_for_work as global_data
import Salvador_Sakho.l_1_functions.Home_work.keys_handler as keys_handler
from copy import copy

global_data.init()


def handle_dict_data(dictionary, action=None, **collection):
    temp_dict = copy(dictionary)
    for key, val in temp_dict.items():
        keys_handler.check_key(dictionary, key)
        if type_handler.check_if_dict(val):
            handle_dict_data(val, collection=collection, action=action)
        elif type_handler.check_if_list(val):
            list_handler.handle_list_data(val, key=key, main_list=collection, action=action)
        elif type_handler.check_if_string(val) \
                or type_handler.check_if_boolean(val) \
                or type_handler.check_if_int(val) \
                or type_handler.check_if_float(val):
            action_handler.handle_action(collection=dictionary, key=key, value=val, action=action)


def to_dict(key, val):
    if key in global_data.main_dict.keys():
        global_data.main_dict[key].append(val if val is not None else None)
    else:
        global_data.main_dict[key] = [val if val is not None else None]


def campaign_id_case_handler(list_comp):
    list_handler.handle_list_data(list_comp, main_dict=global_data.main_dict, action='to_dict')
    return global_data.main_dict['campaign_id']


def metric_sums_case_handler(list_comp):
    list_handler.handle_list_data(list_comp, main_dict=global_data.main_dict, action='to_dict')
    dict_sum = global_data.main_dict['sum']
    dict_sum_level = global_data.main_dict['sum_level']
    dict_sum_general = global_data.main_dict['sum_general']
    continuing_calculations(dict_sum, dict_sum_level, dict_sum_general, sum_funk=sum_funk, avg_funk=avg_funk)


def continuing_calculations(*args, **continuing_func_to_perform):
    for data in args:
        continuing_func_to_perform['avg_funk'](continuing_func_to_perform['sum_funk'](data), len(data))


def avg_funk(value, data_len):
    print(f'AVG of values: {value / data_len}')
    return value / data_len


def sum_funk(*data):
    print(f'Sum of values: {reduce(lambda a, b: a + b, data[0])}')
    return reduce(lambda a, b: a + b, data[0])


def report_name_case_handler(list_comp):
    list_handler.handle_list_data(list_comp, main_dict=global_data.main_dict, action='to_dict')
    for idx, data in enumerate(global_data.main_dict['report_name']):
        if data == 'device':
            global_data.main_dict['report_name'][idx] = data.upper()
    return global_data.main_dict


def page_id_case_handler(list_comp):
    list_handler.handle_list_data(list_comp, main_dict=global_data.main_dict, action='to_dict')
    for idx, data in enumerate(global_data.main_dict['page_id']):
        if data == '(not set)':
            global_data.main_dict['page_id'][idx] = None
    return global_data.main_dict
