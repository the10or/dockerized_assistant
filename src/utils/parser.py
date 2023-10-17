import re
import difflib
from .constants import BOT_COMMANDS


def parser(line):
    data_array = list(filter(None, re.split('|'.join(BOT_COMMANDS), line)))
    command = difflib.get_close_matches(line, BOT_COMMANDS, n=1, cutoff=0.1)
    if not len(command):
        raise AttributeError
    data = data_array[0].strip().split(' ') if len(data_array) > 0 else None

    return command[0], data
