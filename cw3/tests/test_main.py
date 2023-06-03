import json
import pytest
from cw3 import hidden_number, executed_operations, message, format_date
@pytest.fixture
def operation_list():
    return [
        {
            'state': 'EXECUTED',
            'date': '2023-05-20T08:30:00',
            'from': '1234567890123456',
            'to': '9876543210987654',
            'description': 'Payment',
            'operationAmount': {
                'amount': 100.0,
                'currency': {'name': 'USD'}
            }
        },
        {
            'state': 'PENDING',
            'date': '2023-05-21T10:00:00',
            'from': '9876543210987654',
            'to': '1234567890123456',
            'description': 'Transfer',
            'operationAmount': {
                'amount': 200.0,
                'currency': {'name': 'EUR'}
            }
        }
    ]





def test_get_executed_operations(operation_list):
    executed_operation = executed_operations.get_executed_operations(operation_list)
    assert len(executed_operation) == 1
    assert executed_operation[0]['state'] == 'EXECUTED'


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

def test_format_date():
    formatted_date = format_date.format_date('2023-05-20T08:30:00')
    assert formatted_date == '20.05.2023'


def test_get_message():
    operation_1 = {
    "id": 801684332,
    "state": "EXECUTED",
    "date": "2019-11-05T12:04:13.781725",
    "operationAmount": {
      "amount": "21344.35",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Открытие вклада",
    "to": "Счет 77613226829885488381"
  }
    operation_2 = {
    "id": 154927927,
    "state": "EXECUTED",
    "date": "2019-11-19T09:22:25.899614",
    "operationAmount": {
      "amount": "30153.72",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод организации",
    "from": "Maestro 7810846596785568",
    "to": "Счет 43241152692663622869"
  }

    assert message.get_message(operation_1) == "05.11.2019 Открытие вклада\nСчёт отправителя неизвестен -> Счет **8381\n21344.35 руб. \n"
    assert message.get_message(operation_2) == "19.11.2019 Перевод организации\nMaestro 7810 84** **** 5568 -> Счет **2869\n30153.72 руб. \n"