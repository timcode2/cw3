from cw3 import hidden_number

def test_format_from_account():
    assert hidden_number.format_from_account('Счет 1234567890123456') == 'Счет 1234 56** **** 3456'
    assert hidden_number.format_from_account('Счет 12345678901234567890') == 'Счет 1234 56** **** 7890'
    assert hidden_number.format_from_account('МИР 1234567890123456') == 'МИР 1234 56** **** 3456'
    assert hidden_number.format_from_account('МИР 12345678901234567890') == 'МИР 1234 56** **** 7890'
    assert hidden_number.format_from_account('Visa Platinum 1234567890123456') == 'Visa Platinum 1234 56** **** 3456'
    assert hidden_number.format_from_account('Visa Platinum 12345678901234567890') == 'Visa Platinum 1234 56** **** 7890'
    assert hidden_number.format_from_account('Visa Classic 1234567890123456') == 'Visa Classic 1234 56** **** 3456'
    assert hidden_number.format_from_account('Visa Classic 12345678901234567890') == 'Visa Classic 1234 56** **** 7890'
    assert hidden_number.format_from_account('Visa Gold 1234567890123456') == 'Visa Gold 1234 56** **** 3456'
    assert hidden_number.format_from_account('Visa Gold 12345678901234567890') == 'Visa Gold 1234 56** **** 7890'

def test_format_to_account():
    assert hidden_number.format_to_account('Счет 1234567890123456') == 'Счет **3456'
    assert hidden_number.format_to_account('Счет 12345678901234567890') == 'Счет **7890'
    assert hidden_number.format_to_account('МИР 1234567890123456') == 'МИР **3456'
    assert hidden_number.format_to_account('МИР 12345678901234567890') == 'МИР **7890'
    assert hidden_number.format_to_account('Visa Platinum 1234567890123456') == 'Visa Platinum **3456'
    assert hidden_number.format_to_account('Visa Platinum 12345678901234567890') == 'Visa Platinum **7890'
    assert hidden_number.format_to_account('Visa Classic 1234567890123456') == 'Visa Classic **3456'
    assert hidden_number.format_to_account('Visa Classic 12345678901234567890') == 'Visa Classic **7890'
    assert hidden_number.format_to_account('Visa Gold 1234567890123456') == 'Visa Gold **3456'
    assert hidden_number.format_to_account('Visa Gold 12345678901234567890') == 'Visa Gold **7890'