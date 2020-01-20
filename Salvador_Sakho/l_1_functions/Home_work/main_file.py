import Salvador_Sakho.l_1_functions.Home_work.keys_handler as keys_handler
import Salvador_Sakho.l_1_functions.Home_work.list_handler as list_handler
from Salvador_Sakho.l_1_functions.Home_work.dict_handler import metric_sums_case_handler
from Salvador_Sakho.l_1_functions.hw_start import insights
import Salvador_Sakho.l_1_functions.Home_work.globals_for_work as global_data

global_data.init()
# "Raise error" нужно ли?
list_comp = [line for line in insights]

if __name__ == '__main__':
    list_handler.handle_list_data(list_comp, main_list=global_data.main_list, action='to_list')
    list_handler.handle_list_data(list_comp, main_dict=global_data.main_dict, action='to_dict')
    list_handler.handle_list_data(list_comp, action='campaign_id_collect')
    list_handler.handle_list_data(list_comp, action='to_set')

    print(global_data.main_list)
    print(global_data.campaign_id_dict)
    print(global_data.main_set)
    print(metric_sums_case_handler())

    keys_handler.remove_keys(list_comp, ('period', 'count', 'total_count', 'page_id', 'link', 'status',
                                         'days_in_data', ('table_columns', 'unit', 'EUR')
                                         , ('metric_sums', 'unit_key', 'EUR')))
