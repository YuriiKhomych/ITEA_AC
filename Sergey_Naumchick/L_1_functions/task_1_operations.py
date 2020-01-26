import configures


# # Task #1 (A)

# def remove_unused_keys(insights):
#     if type(insights) == dict:
#         insights_copy = insights.copy()
#         for key, value in insights_copy.items():
#             if key == configures.KEYS_TO_REM_ROOT_LVL:
#                 del insights[key]
#
#     if type(insights) == list:
#         for dicts in insights:
#             remove_unused_keys(dicts)
#
#     return insights


# # Task #1 (B)

def entities_lvl_remova(insights):
    if isinstance(insights, dict):
        insights_copy = insights.copy()
        for key, value in insights_copy.items():
            if key == "entities_affected":
                find_in_ent_eff(value)

    if type(insights) == list:
        for dicts in insights:
            entities_lvl_remova(dicts)

    return insights


def find_in_ent_eff(insights):
    if isinstance(insights, dict):
        insights_copy = insights.copy()
        for key, value in insights_copy.items():
            if key in configures.KEY_TO_REM_ENT_AFFEC:
                del insights[key]
            else:
                find_in_ent_eff(value)

    elif isinstance(insights, list):
        for dicts in insights:
            find_in_ent_eff(dicts)
    return insights
