import json
import os
import const


def import_data_json(filename):
    with open(filename) as file:
        pop_data = json.load(file)

        return pop_data


def analyzer(datas):
    for key, value in datas.items():
        if key == "breakdowns":
            list_items_to_search = value
        if key == "project_id_to_project_execution":
            dict_id = value

    for project_id, project_execution_id in dict_id.items():
        for exec_id in project_execution_id:
            string_1 = f"analyzer/project_id-{project_id}/" \
                       f"project_execution-{exec_id}/" \
                       f"2-function_name-generate_nb_insights"

            try:
                with os.scandir(string_1) as entries:
                    for entry in entries:
                        if entry.name.endswith("-1.json"):
                            with open(f"{string_1}/{entry.name}") as file2:
                                pop_data2 = json.load(file2)
                                const.answer_1.append(search_in_dict(pop_data2, list_items_to_search))
            except Exception as e:
                print(f"no such file - {e}")


# searching in json file and return count of similar in list
s_count = []


def search_in_dict(my_json, my_list):
    if isinstance(my_json, dict):

        for key, value in my_json.items():

            if key == "name":
                for val in my_list:
                    s = f"dimension:{val}"
                    if value == s:
                        s_count.append(value)

            if key == "dimensions":
                search_in_dict(value, my_list)

    if isinstance(my_json, list):
        for dicts in my_json:
            search_in_dict(dicts, my_list)

    return s_count


if __name__ == '__main__':
    analyzer(import_data_json("input_data.json"))
    print(const.answer_1)
