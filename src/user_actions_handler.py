from error_handler import input_error
from address_book.contact_book import AddressBook
import globals
from file_config import file_contact_book, file_notes
import pickle

try:
    with open(file_contact_book, "rb") as fh:
        unpacked = pickle.loads(fh.read())
        book = unpacked
except FileNotFoundError:
    book = AddressBook()

try:
    with open(file_notes, "rb") as fh:
        unpacked = pickle.loads(fh.read())
        book = unpacked
except FileNotFoundError:
    notes = 'class Notes here'  # TODO: add class Notes


@input_error
def handler_show_all_contacts(*args):
    pass


def handler_greetings(*args):
    return 'How can I help you?'


def handler_bye(*args):
    globals.is_listening = False
    return 'Good bye!'


def handler_add_contact(data):
    pass


def get_handler(operator):
    return OPERATORS[operator]


OPERATORS = {
    'hello': handler_greetings,
    'hi': handler_greetings,
    'close': handler_bye,
    'exit': handler_bye,
    'good bye': handler_bye,
    'add contact': handler_add_contact
}
