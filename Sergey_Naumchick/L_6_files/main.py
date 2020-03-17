import json, os, const, csv


def import_data_json(filename):
    with open(filename) as file:
        return json.load(file)


def analyzer(datas):
    for key, value in datas.items():
        if key == "breakdowns":
            list_items_to_search = value
        if key == "project_id_to_project_execution":
            dict_id = value

    # first part -1.json
    list_with_dimension_add = []

    for word in list_items_to_search:
        list_with_dimension_add.append(f"dimension:{word}")

    for project_id, project_execution_id in dict_id.items():
        for exec_id in project_execution_id:
            string_1 = f"analyzer/project_id-{project_id}/" \
                       f"project_execution-{exec_id}/" \
                       f"2-function_name-generate_nb_insights"

            with os.scandir(string_1) as entries:
                for entry in entries:
                    if entry.name.endswith("-1.json"):
                        list_considentions = []
                        list_all = []
                        with open(f"{string_1}/{entry.name}") as file_json:
                            pop_data2 = json.load(file_json)
                            result = search_in_dict(pop_data2,
                                                    list_with_dimension_add,
                                                    list_all,
                                                    list_considentions)
                            const.answer_1[f"{project_id}, {exec_id}"] = [len(result[0]), len(result[1])]

    # seconf part - mid

    with os.scandir("mid") as entries:
        for entry in entries:
            with open(f"mid/{entry.name}") as file_csv:
                reader = csv.DictReader(file_csv)
                list_reader = []
                list_all = []
                for row in reader:
                    for keys, values in row.items():
                        if keys == "dimensions":
                            json_dict = values.replace("'", '"')
                            dict_val_dimensions = json.loads(json_dict)

                            for k, v in dict_val_dimensions.items():
                                list_all.append(k)
                                if k in list_items_to_search:
                                    list_reader.append(v)
            const.answer_2.append(list_reader)
            const.answer_2_all.append(list_all)

    # third part - final_results

    with os.scandir("final_results") as entr:
        for e in entr:
            with open(f"final_results/{e.name}") as f_json:
                pop_data3 = json.load(f_json)
                list_all_csv = []
                list_coincidences_csv = []
                const.answer_3.append(search_in_dict(pop_data3,
                                                     list_items_to_search,
                                                     list_all_csv,
                                                     list_coincidences_csv))


# searching in json file and return count of similar in list


def search_in_dict(my_json, my_list, count_all, count_coincidences):
    if isinstance(my_json, dict):

        for key, value in my_json.items():
            count_all.append(key)
            if key == "name":
                if value in my_list:
                    count_coincidences.append(value)

            if key == "dimensions":
                search_in_dict(value, my_list, count_all, count_coincidences)

    if isinstance(my_json, list):
        for dicts in my_json:
            search_in_dict(dicts, my_list, count_all, count_coincidences)
    return count_all, count_coincidences


if __name__ == '__main__':
    analyzer(import_data_json("input_data.json"))

    print(const.answer_3)
    for key, value in const.answer_1.items():
        for k in const.answer_2_all:
            for x in const.answer_2:
                for a in const.answer_3:
                    list_1 = key.split(", ")
                    print(f"project_id: {list_1[0]}, project_execution_id: {list_1[1]}")
                    print(f"analyzer_insights_len: {value[0]}")
                    print(f"analyzer_insights_with_br_len: {value[1]}")
                    print(f"mid_insights_len: {len(k)}")
                    print(f"mid_insights_with_br_len: {len(x)}")
                    print(f"final_insights_len: {len(a[0])}")
                    print(f"final_insights_with_br_len: {len(a[1])}")
