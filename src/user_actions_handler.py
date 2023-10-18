from pathlib import Path

from .error_handler import input_error
from .address_book.contact_book import AddressBook
from . import globals
from .utils.constants import WARNING_MESSAGE, ABORTING_OPERATION_MESSAGE, SORTING_PROGRESS_MESSAGE
from .file_config import FILE_CONTACT_BOOK, FILE_NOTES
import pickle
from .sort_file import sort


def get_book():
    try:
        with open(FILE_CONTACT_BOOK, "rb") as fh:
            unpacked = pickle.loads(fh.read())
            return unpacked
    except FileNotFoundError:
        return AddressBook()


book = get_book()


def get_notes():
    try:
        with open(FILE_NOTES, "rb") as fh:
            unpacked = pickle.loads(fh.read())
            return unpacked
    except FileNotFoundError:
        return 'class Notes here'  # TODO: add class Notes


notes = get_notes()


@input_error
def handler_show_all_contacts(*args):
    pass


def handler_greetings(*args):
    return "How can I help you?"


def handler_bye(*args):
    globals.IS_LISTENING = False
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
    choice = input(WARNING_MESSAGE)
    if choice.lower() == "n":
        return ABORTING_OPERATION_MESSAGE

    # Print progress message
    print(SORTING_PROGRESS_MESSAGE + dir_path[0])

    # Sort the directory
    sort.main(Path(dir_path[0]))

    return "Done!"


def handler_add_contact(data):
    pass


@input_error
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
