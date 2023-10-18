from pathlib import Path

from error_handler import input_error
from address_book import contact_book
from address_book.contact_book import AddressBook
from record import Record
import globals
from utils.constants import WARNING_MESSAGE, ABORTING_OPERATION_MESSAGE, SORTING_PROGRESS_MESSAGE
from file_config import file_contact_book, file_notes
from sort_file import sort


book = AddressBook()

def notes():
    ...

def handler_greetings(*args):
    return "How can I help you?"


def handler_bye(*args):
    globals.is_listening = False
    return "Good bye!"


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


@input_error
def handler_add_contact(name):
    '''usage: 

    add contact [firstname] [surname]
    or: add contact [name]

    names should not include numbers!!'''
    print(name)
    return book.add_record(name)


@input_error
def handler_show_all(input):
    '''usage:
        show all'''
    out = "Contacts found:\n"
    name = book.find_all("")
    for n in name:
        out += f"{n}\n"
    if len(name) > 0:
        return out
    else:
        return "Contact list is empty"    


@input_error
def handler_add_phone(arg: list):
    '''usage:
        add phone [name] [phone]
    phones should be either 7 or 10 char long'''
    name, phone = arg
    result = book.get(name.lower()).add_phone(phone)
    return result


@input_error
def handler_search(input):
    '''usage:
        search contacts [any str or int]'''
    if len(input) == 1:
        input = input[0]
        out = "Contacts found:\n"
        results = book.find_all(input)
        for res in results:
            out += f"{res}\n"
        if len(results) > 0:
            return out
        else:
            return "Contact list is empty"
    else:
        raise ValueError("Wrong search input")

@input_error
def handler_find(input: list):
    '''usage:
        find contact [name]
    or  find contact [first name] [second name]'''
    if len(input) == 1:
        input = input[0]
        return book.find(input.lower())
    elif len(input) == 2:
        name, surname = input
        return book.find(f"{name.lower()}, {surname.lower()}")
    else:
        raise ValueError("Wrong find input")    

@input_error
def handler_change_birthday(arg):
    '''usage: 
        change birthday [name] [new birthday in format xx/xx/xxxx]'''
    name, birthday = arg
    if book.get(name.lower(), None):
        book.get(name.lower(), None).edit_birthday(birthday)
        return f"Changed birthday to {birthday}"
    else:
        return "Contact does not exist"
    
def handler_delete_contact(input):
    if len(input) == 1:
        name = input[0]
        book.delete(name.lower())
        return f"Contact {name} deleted"
    elif len(input) == 2:
        name, surname = input
        book.delete(f"{name.lower()}, {surname.lower()}")
        return f"Contact {name}, {surname} deleted"
    else:
        return "Contact not found"


def get_handler(operator):
    return OPERATORS[operator]


OPERATORS = {
    "hello": handler_greetings,
    "hi": handler_greetings,
    "close": handler_bye,
    "exit": handler_bye,
    "good bye": handler_bye,
    "sort dir": handler_sort,
    "add contact": handler_add_contact,
    "show all": handler_show_all,
    "add phone": handler_add_phone,
    "change birthday": handler_change_birthday,
    "search contacts": handler_search,
    "find contact": handler_find,
    "delete contact": handler_delete_contact
}
