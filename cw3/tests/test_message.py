from cw3 import message

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