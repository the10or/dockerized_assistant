from user_actions_handler import get_handler
import globals
from utils.parser import parser, COMMANDS
from user_actions_handler import book, notes
import pickle
from file_config import file_contact_book, file_notes

BOT_COMMANDS = 'hello\n' \
               'close\n' \
               'exit\n'


def main():
    print(f'use those commands:\n{BOT_COMMANDS}\n')
    while globals.is_listening:
        user_line = input(f'listening...\n')
        if user_line is not None:
            try:
                command, data = parser(user_line)
                handler = get_handler(command)
                result = handler(data)
                print(result)
                with open(file_contact_book, "wb") as fh:
                    fh.write(pickle.dumps(book))
                with open(file_notes, "wb") as fh:
                    fh.write(pickle.dumps(notes))
                continue
            except AttributeError:
                print(f'Please, type one of the commands: {COMMANDS}')


if __name__ == '__main__':
    main()
