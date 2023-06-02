import json


def get_input_data(file_name):
    """
    :param file_name: Название json-файла с исходными данными
    :return: данные json-файла в виде списка словарей
    """
    with open(file_name, 'r', encoding='utf-8') as f:
        input_data = json.load(f)
    return input_data
