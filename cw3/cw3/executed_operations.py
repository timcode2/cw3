def get_executed_operations(operation_list):
    """
    Функция определяет статуст перевода
    :param operation_list: Список со словарями с данными по операциям
    :return: Список из 5 успешных операций
    """
    executed_operations = []
    for operation in operation_list:
        if 'state' in operation.keys():
            if operation['state'] == 'EXECUTED':
                executed_operations.append(operation)
        else:
            continue
    return executed_operations[0:5]