import Salvador_Sakho.l_1_functions.Home_work.action_handler as action_handler
from Salvador_Sakho.l_1_functions.hw_start import insights
import Salvador_Sakho.l_1_functions.Home_work.globals_for_work as global_data

global_data.init()
list_comp = [line for line in insights]

# todo: 8, 11(не ясна задача)

if __name__ == '__main__':
    action_handler.run_process(list_comp, action='entities_to_list')
    print(global_data.entities_spend_sum)
    # keys_handler.check_and_manage(list_comp, 'entities')
    # keys_handler.remove_keys(list_comp, )

    # print(list_handler.objective_case_handler(list_comp))
    # print(dict_handler.campaign_id_case_handler(list_comp))
    # dict_handler.metric_sums_case_handler(list_comp)
    # print(set_handler.objective_case_handler(list_comp))
    # print(dict_handler.report_name_case_handler(list_comp))
    # print(dict_handler.page_id_case_handler(list_comp))
