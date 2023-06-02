def format_date(input_date):
    """
    Форматирует дату и время операции оставляя только дату в нужном формате
    :param input_date: Строка с данными о дате и времени операции
    :return: Строка с данными о дате в заданном формате
    """
    date_list = input_date[0:10].split('-')
    return '.'.join(date_list[::-1])
