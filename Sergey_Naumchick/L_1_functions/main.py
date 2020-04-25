from hw_start import insights
import configures
import task_1_operations
import task_2_operations
import task_3_operations
import task_4_5_operations
import task_6_operstions
import task_7_operations
import task_8_operations
import task_9_operations
import task_10_operations
import task_11_operations

""" 1. Remove unused keys from insight like:"""
# A:

# print(task_1_operations.remove_unused_keys(insights))

# B:

# print(task_1_operations.entities_lvl_remova(insights))

""" 2. Remove keys which not fit the condition:"""

# A:

# print(task_2_operations.search_in_dict(insights))

""" 3. Get all insights objectives into list of strings result:"""

# print(task_3_operations.search_in_dict(insights))

""" 4.,5. Get all insights objectives into dict of strings:"""

# print(task_4_5_operations.search_in_dict(insights))

""" 6. Get all unique insights objectives:"""

# print(task_6_operstions.search_in_dict(insights))

""" 7. Get all unique insights objectives:"""

# print(task_7_operations.get_all_insig_metr_sum(insights))

""" 8. Sort list of insights by "type", "api", "report_name" and "objective"""

# print(task_8_operations.sorting_by(insights, "type"))
# print(task_8_operations.sorting_by(insights, "api"))
# print(task_8_operations.sorting_by(insights, "report_name"))
# print(task_8_operations.sorting_by(insights, "objective"))

""" 9. If "report_name" equal "device" make this value uppercase:"""

# print(task_9_operations.search_in_dict(insights))

""" 10. If "page_id" equal "(not set)" replace it by None:"""

# print(task_10_operations.search_in_dict(insights))

""" 11. If "page_id" equal "(not set)" replace it by None:"""

print(task_11_operations.calc_summary(insights))
