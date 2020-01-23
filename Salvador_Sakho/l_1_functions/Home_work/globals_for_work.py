def init():
    global main_list
    main_list = []
    global main_dict
    main_dict = {}
    global general_id
    general_id = 0
    global campaign_id_dict
    campaign_id_dict = {'campaign_id': []}
    global main_set
    main_set = set()
    global keys_for_remove
    keys_for_remove = ('period', 'count', 'total_count', 'page_id', 'link', 'status',
                       'days_in_data', ('table_columns', 'unit', 'EUR')
                       , ('metric_sums', 'unit_key', 'EUR'))
    global entities_spend_sum
    entities_spend_sum = []
