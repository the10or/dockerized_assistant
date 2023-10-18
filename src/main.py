from .user_actions_handler import get_handler, book, notes
from .utils.constants import BOT_COMMANDS
from . import globals
from .utils.parser import parser
import pickle
from file_config import FILE_NOTES


def main():
    print(
        f"use these commands:\n{BOT_COMMANDS}\n"
    )
    while globals.IS_LISTENING:
        user_line = input(f"::> ")
        if user_line:
            try:
                command, data = parser(user_line)
                handler = get_handler(command)
                result = handler(data)
                print(result)
                with open(FILE_NOTES, "wb") as fh:
                    fh.write(pickle.dumps(notes))
                continue            
            except AttributeError:
                print(f'Please, type one of the commands: {BOT_COMMANDS}')


if __name__ == "__main__":
    main()
