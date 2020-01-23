"""Homework 1"""

""" 1. Remove unused keys from insight like:"""
# A: On root level remove:

keys_to_rem_root_lvl = ["period", "count", "total_count", "page_id"]
list_deleted_1_a = []

# B: On entities_affected -> entities level remove:
key_to_rem_ent_affec = ["link", "status", "days_in_data"]
list_deleted_1_b = []

""" 2. Remove keys which not fit the condition:"""
# A: Remove each element from "table_columns" where "unit" not equal to "EUR"

key_to_rem_not_cond = "EUR"
name_label = "table_columns"
search_key_n_eq = "unit"
list_unit_not_eq = []

# B: Remove each element from "metric_sums" where "unit_key" not equal to "EUR"

# key_to_rem_not_cond = "EUR"
# name_label = "metric_sums"
# search_key_n_eq = "unit_key"
# list_unit_not_eq = []

""" 3. Get all insights objectives into list of strings result: ["objective_1", "objective_2"]"""

get_values_of_key = "objective"
list_values_of_key = []

""" 4.,5. Get all insights objectives into dict result: [{"objective": "objective_1"}, {"objective": "objective_2"},]"""

get_values_of_key_d = "campaign_id"
dict_values_of_key = {}
list_values_of_key_d = []

""" 6. Get all insights objectives into dict result: [{"objective": "objective_1"}, {"objective": "objective_2"},]"""

key_for_unique = "objective"
list_unique_values = []

""" 7. Get all insights "metric_sums" and calculate sum and average:"""

key_metric_sums = "metric_sums"

list_metric_names = []
list_metric_sum = []
list_metric_sum_level = []
list_metric_general = []

list_metric_answer = []

""" 9. If "report_name" equal "device" make this value uppercase:"""
