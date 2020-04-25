"""Homework 1"""

""" 1. Remove unused keys from insight like:"""
# A: On root level remove:

KEYS_TO_REM_ROOT_LVL = ("period", "count", "total_count", "page_id")

# B: On entities_affected -> entities level remove:
KEY_TO_REM_ENT_AFFEC = ("link", "status", "days_in_data")

""" 2. Remove keys which not fit the condition:"""
# A: Remove each element from "table_columns" where "unit" not equal to "EUR"

KEY_TO_REM_NOT_COND = "EUR"
NAME_LABEL = "table_columns"  # "metric_sums"
SEARCH_KEY_N_EQ = "unit"  # "unit_key"

# B: Remove each element from "metric_sums" where "unit_key" not equal to "EUR"

# key_to_rem_not_cond = "EUR"
# name_label = "metric_sums"
# search_key_n_eq = "unit_key"
# list_unit_not_eq = []

""" 3. Get all insights objectives into list of strings result: ["objective_1", "objective_2"]"""

GET_VALUES_OF_KEY = "objective"
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

""" 10. If "report_name" equal "device" make this value uppercase:"""

""" 11. Calculate summary by formulas (if root "period" > 4 or None set default root "period" as 7):"""
