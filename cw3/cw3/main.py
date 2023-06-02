from cw3.cw3 import opendata
from cw3.cw3 import executed_operations
from cw3.cw3 import message


data_list = opendata.get_input_data('../operations.json')

operations = executed_operations.get_executed_operations(data_list)

for operetion in operations:
    print(message.get_message(operetion))

