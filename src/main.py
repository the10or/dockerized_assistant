import pickle
import globals
from file_config import FILE_CONTACT_BOOK, FILE_NOTES
from utils.constants import INVITE_MESSAGE, TYPE_OR_ATTRIBUTE_ERROR_MESSAGE, UNDEFINED_ERROR_MESSAGE
from user_actions_handler import get_handler, book, notes
from utils.parser import parser


def main():
    while globals.IS_LISTENING:

        user_line = input(INVITE_MESSAGE)
        if user_line:
            try:
                command, data = parser(user_line)
                handler = get_handler(command)
                result = handler(data)
                print(result)
                with open(FILE_CONTACT_BOOK, "wb") as fh:
                    fh.write(pickle.dumps(book))
                with open(FILE_NOTES, "wb") as fh:
                    fh.write(pickle.dumps(notes))
                continue
            except (AttributeError, TypeError):

                print(f'{TYPE_OR_ATTRIBUTE_ERROR_MESSAGE} \n{get_handler('help')()}')

            except Exception as error:

                print(f"{UNDEFINED_ERROR_MESSAGE} {error}")


if __name__ == "__main__":
    main()
