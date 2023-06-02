def format_from_account(input_from_account):
    '''
    Функция скрывает номер карты отправителя
    :param input_from_account: Номер счёта отправителя
    :return: Скрытый счёт отправителя
    '''
    from_account_split = input_from_account.split(" ")
    new_str = ' ' + from_account_split [-1][0:4] + ' ' + from_account_split [-1][4:6] + '** ' + '**** ' + from_account_split [-1][12:16]
    return from_account_split[0] + new_str


def format_to_account(input_to_account):
    """
    Функция скрывает номер карты получателя
    :param input_to_account: Номер счёта получателя
    :return: Скрытый счёт получателя
    """
    to_account_split = input_to_account.split(" ")
    new_str = ' **' + to_account_split[1][16:20]
    return to_account_split[0] + new_str
