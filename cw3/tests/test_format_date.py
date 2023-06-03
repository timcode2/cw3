from cw3 import format_date

def test_format_date():
    formatted_date = format_date.format_date('2023-05-20T08:30:00')
    assert formatted_date == '20.05.2023'
