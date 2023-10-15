import re
import difflib

COMMANDS = ['hi', 'hello', 'close', 'exit', 'good bye', 'add contact', 'find birthday', 'find contact', 'remove phone',
            'remove address', 'remove birthday', 'remove email', 'edit phone', 'edit address', 'edit birthday',
            'edit email', 'delete contact', 'add note', 'find note', 'edit note title', 'edit note text',
            'add note tag', 'delete note', 'sort note', 'sort files']


def parser(line):
    data_array = list(filter(None, re.split('|'.join(COMMANDS), line)))
    command = difflib.get_close_matches(line, COMMANDS, n=1, cutoff=0.1)
    if not len(command):
        raise AttributeError
    data = data_array[0].strip().split(' ') if len(data_array) > 0 else None
    return command[0], data
