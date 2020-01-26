import configures


def search_in_dict(dicta):
    if type(dicta) == dict:
        for key, value in dicta.items():
            if key == configures.key_metric_sums:
                search_in_m_sums(value)
            else:
                search_in_dict(value)
    elif type(dicta) == list:

        for dicts in dicta:
            search_in_dict(dicts)


def search_in_m_sums(d_key):
    if type(d_key) == dict:

        for key, value in d_key.items():
            if key == "metric_name":
                configures.list_metric_names.append(value)
            elif key == "sum":
                configures.list_metric_sum.append(value)
            elif key == "sum_level":
                configures.list_metric_sum_level.append(value)
            elif key == "sum_general":
                configures.list_metric_general.append(value)

    elif type(d_key) == list:
        for dicta in d_key:
            search_in_m_sums(dicta)


def get_all_insig_metr_sum(list_dicts):
    search_in_dict(list_dicts)
    for i in range(len(configures.list_metric_names)):
        configures.list_metric_answer.append(
            f"Metric name - {(configures.list_metric_names[i]).upper()} the sum is - {configures.list_metric_sum[i] + configures.list_metric_sum_level[i] + configures.list_metric_general[i]}")

    return configures.list_metric_answer
