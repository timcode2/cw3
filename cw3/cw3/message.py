from cw3.cw3 import hidden_number
from cw3.cw3 import format_date

def get_message(operation):
    '''
    Функция создаст структуру выводящего сообщения
    :param operation: Работаем со словарём файла operations.json
    :return: Готовое сообщение с данными
    '''
    date = format_date.format_date(operation['date'])
    description = operation['description']
    if 'from' not in operation.keys():
        from_account = 'Счёт отправителя неизвестен'
    else:
        from_account = hidden_number.format_from_account(operation['from'])
    to_account = hidden_number.format_to_account(operation['to'])
    amount = operation['operationAmount']['amount']
    currency = operation['operationAmount']['currency']['name']

    first_line_list = [date, description]
    second_line_list = [from_account, '->', to_account]
    third_line_list = [amount, currency, '\n']

    first_line = ' '.join(first_line_list)
    second_line = ' '.join(second_line_list)
    third_line = ' '.join(third_line_list)

    return '\n'.join([first_line, second_line, third_line])
