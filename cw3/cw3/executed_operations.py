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
                date = operation.get('date')
                formatted_date = date[:10]
                executed_operations.append((formatted_date, operation))
            else:
                continue

    sorted_operations = sorted(executed_operations, key=lambda x: x[0], reverse=True)
    last_five_operations = [operation[1] for operation in sorted_operations[:5]]
    print(last_five_operations)
    return last_five_operations
