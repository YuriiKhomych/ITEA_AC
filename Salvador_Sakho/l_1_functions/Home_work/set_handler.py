import Salvador_Sakho.l_1_functions.Home_work.globals_for_work as global_data
from Salvador_Sakho.l_1_functions.Home_work import list_handler

global_data.init()


def to_set(*data):
    global_data.main_set.add(data)


def objective_case_handler(list_comp):
    list_handler.handle_list_data(list_comp, main_dict=global_data.main_dict,
                                  action='to_dict')
    return set(global_data.main_dict['objective'])
