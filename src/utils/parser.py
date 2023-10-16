import re

COMMANDS_RGX = 'hello|close|exit|' \
               'add contact|' \
               'change phone|' \
               'show all|' \
               'get phone|' \
               'get birthday|' \
               'search contact' 
               


def parser(line):
    data_array = list(filter(None, re.split(COMMANDS_RGX, line)))
    command = re.search(COMMANDS_RGX, line)

    data = data_array[0].strip().split(' ') if len(data_array) > 0 else None
    return command.group(), data
