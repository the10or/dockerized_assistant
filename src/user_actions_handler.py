from error_handler import input_error
from address_book.contact_book import AddressBook
import globals
from file_config import file
import pickle
from sort_file import sort

try:
    with open(file, "rb") as fh:
        unpacked = pickle.loads(fh.read())
        book = unpacked
except FileNotFoundError:
    book = AddressBook()


@input_error
def handler_show_all_contacts(*args):
    pass


def handler_greetings(*args):
    return 'How can I help you?'


def handler_bye(*args):
    globals.is_listening = False
    return 'Good bye!'


def handler_sort(dir):
    sort.main(dir)


def get_handler(operator):
    return OPERATORS[operator]


OPERATORS = {
    'hello': handler_greetings,
    'close': handler_bye,
    'exit': handler_bye,
    'sort dir': handler_sort
}
