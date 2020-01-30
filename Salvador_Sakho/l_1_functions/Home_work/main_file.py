import Salvador_Sakho.l_1_functions.Home_work.action_handler as action_handler
from Salvador_Sakho.l_1_functions.hw_start import insights

# todo: 7, 10 

if __name__ == '__main__':
    # remove_key
    # entities_to_list -> check entities_spend_sum ???
    # to_dict -> check main_dict
    # to_list -> check main_list
    # to_set -> check main_set
    # objective_case -> check main_set
    # campaign_id -> check main_dict
    # metric_sums_case -> will print result for all metrix
    # report_name_case -> check main_dict
    # page_id_case -> check main_dict

    ah = action_handler.HandleAction()
    ah.run_process([line for line in insights], action='page_id_case')
    print(ah.main_dict['page_id'])
