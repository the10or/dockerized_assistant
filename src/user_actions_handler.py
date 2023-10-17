from pathlib import Path

from error_handler import input_error
from address_book.contact_book import AddressBook
import globals
from file_config import file_contact_book, file_notes
import pickle
from sort_file import sort

try:
    with open(file_contact_book, "rb") as fh:
        unpacked = pickle.loads(fh.read())
        book = unpacked
except FileNotFoundError:
    book = AddressBook()

try:
    with open(file_notes, "rb") as fh:
        unpacked = pickle.loads(fh.read())
        notes = unpacked
except FileNotFoundError:
    notes = 'class Notes here'  # TODO: add class Notes


@input_error
def handler_show_all_contacts(*args):
    pass


def handler_greetings(*args):
    return "How can I help you?"


def handler_bye(*args):
    globals.is_listening = False
    return "Good bye!"


@input_error
def handler_sort(dir_path):
    """
    Handler function for sorting a directory.

    Args:
        dir_path (str): The path of the directory to be sorted.

    Returns:
        str: A message indicating the status of the sorting operation.
    """
    # Prompt the user for confirmation
    choice = input(globals.WARNING_MESSAGE)
    if choice.lower() == "n":
        return globals.ABORTING_OPERATION_MESSAGE

    # Print progress message
    print(globals.SORTING_PROGRESS_MESSAGE + dir_path[0])

    # Sort the directory
    sort.main(Path(dir_path[0]))

    return "Done!"


def handler_add_contact(data):
    pass


def get_handler(operator):
    return OPERATORS[operator]


OPERATORS = {
    "hello": handler_greetings,
    "hi": handler_greetings,
    "close": handler_bye,
    "exit": handler_bye,
    "good bye": handler_bye,
    "sort dir": handler_sort,
    "add contact": handler_add_contact
}
