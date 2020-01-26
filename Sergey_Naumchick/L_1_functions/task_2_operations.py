import configures


# Task #2
def search_in_dict(insights):
    if isinstance(insights, dict):

        for key, value in insights.items():
            if key == configures.NAME_LABEL:
                search_in_dict_label(value)
            else:
                search_in_dict(value)
    elif type(insights) == list:
        for dicts in insights:
            search_in_dict(dicts)
    return insights


def search_in_dict_label(insights):
    if isinstance(insights, dict):
        insights_copy = insights.copy()
        for key, value in insights_copy.items():

            if key == configures.SEARCH_KEY_N_EQ:
                del insights[key]
            else:
                search_in_dict_label(value)
    elif isinstance(insights, list):

        for dicts in insights:
            search_in_dict_label(dicts)
    return insights
