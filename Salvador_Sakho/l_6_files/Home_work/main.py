import json
from collections import defaultdict
import os
import pandas as pd
import ast
import re

breakdowns = []
analyzer_dict_counter = defaultdict(int)
mid_dict_counter = defaultdict(int)
final_results_dict_counter = defaultdict(int)


def dict_handler(collection):
    if 'dimensions_dict' in collection.keys():
        for value in collection['dimensions_dict']:
            if value in breakdowns:
                final_results_dict_counter[value] += 1
    elif 'dimensions' in collection.keys():
        for value in collection['dimensions']:
            for data in value.values():
                if data.replace('dimension:', '') in breakdowns:
                    analyzer_dict_counter[data] += 1
    else:
        for key, value in collection.items():
            if isinstance(value, list):
                list_handler(value)
            elif isinstance(value, dict):
                dict_handler(value)


def list_handler(collection):
    for data in collection:
        if isinstance(data, dict):
            dict_handler(data)
        elif isinstance(data, list):
            list_handler(data)


def json_files_handler(file_path, name):
    with open(f'{file_path}/{name}', 'r') as json_file:
        collection = json.load(json_file)
        if isinstance(collection, list):
            list_handler(collection)
        if isinstance(collection, dict):
            dict_handler(collection)
    return len(collection)


def read_analyzer_files(some_data):
    project_id_project_execution_analyzer = defaultdict(int)
    for key, values in some_data.items():
        for data in values:
            file_path = f'../hw_files/analyzer/project_id-{key}' \
                        f'/project_execution-{data}' \
                        f'/2-function_name-generate_nb_insights'
            for name in [file_name for file_name in os.listdir(file_path)
                         if file_name.find('.json') != -1]:
                project_id_project_execution_analyzer[
                    f'project_execution-{data}'
                ] += json_files_handler(file_path, name)
            print(f"analyzer_files info:\n"
                  f"project_id:{key}, project_execution-id:{data}")
            project_execution_id = f'project_execution-{data}'
            print(f"analyzer_insights_len: "
                  f"{project_id_project_execution_analyzer.get(project_execution_id)}\n")
    print(f'analyzer_insights_with_br_len: {len (analyzer_dict_counter)}')


def data_frame_handler(df):
    for data in df['dimensions'].items():
        for val in ast.literal_eval(data[1]):
            if val in breakdowns:
                mid_dict_counter[val] += 1
    return len(df['dimensions'].to_list())


def read_mid_files():
    project_id_project_execution_mid = defaultdict(int)
    for name in [file_name for file_name in
                 os.listdir(f'../hw_files/mid/')]:
        file_path = f'../hw_files/mid/{name}'
        data_frame = pd.read_csv(file_path, encoding='utf8',
                                 delimiter=',')
        project_id_project_execution_mid[
            f'mid_{name}'.replace('.csv', '')
        ] += data_frame_handler(data_frame)
    print(f'mid_insights: {len(project_id_project_execution_mid.items())}'
          f'\nmid_insights_with_br_len: {len (mid_dict_counter)}')


def read_final_results():
    project_id_project_execution_final_result = defaultdict(int)
    for name in [file_name for file_name
                 in os.listdir(f'../hw_files/final_results/')]:
        project_execution_val = re.search('_(\d+)\.', name).group(1)
        project_id_project_execution_final_result[project_execution_val] \
            += json_files_handler('../hw_files/final_results/', name)
        print(
            f'final_insights {project_execution_val} len: '
            f'{project_id_project_execution_final_result[project_execution_val]}'
        )
    print(
        f'final_insights_with_br_len:{len(final_results_dict_counter)}'
    )


def main():
    project_id_to_project_executions = defaultdict(list)
    with open('../hw_files/input_data.json', 'r') as file:
        json_file = json.load(file)
        # task 1.1
        for data in json_file['breakdowns']:
            breakdowns.append(data)
        for key, value in json_file['project_id_to_project_execution'].items():
            for data in value:
                project_id_to_project_executions[key].append(data)
    # task 1.2
    read_analyzer_files(project_id_to_project_executions)
    print(analyzer_dict_counter, '\n##############')

    # task 1.3
    read_mid_files()
    print(mid_dict_counter, '\n##############')
    # task 1.4
    read_final_results()
    print(final_results_dict_counter, '\n##############')


if __name__ == '__main__':
    main()
