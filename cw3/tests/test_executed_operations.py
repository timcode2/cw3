import pytest
from cw3 import executed_operations
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