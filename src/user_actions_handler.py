from error_handler import input_error
from address_book import contact_book
from address_book.contact_book import AddressBook, Record
import globals
from file_config import file
import pickle

try:
    with open(file, "rb") as fh:
        unpacked = pickle.loads(fh.read())
        book = unpacked
except FileNotFoundError:
    book = AddressBook()

 

@input_error
def handler_greetings(*args):
    return 'How can I help you?'


def handler_bye(*args):
    globals.is_listening = False
    return 'Good bye!'


def get_handler(operator):
    return OPERATORS[operator]


@input_error
def handler_show_all_contacts(*args):
    if not contact_book.data:
        return "No contacts found"
    contact_list = "\n".join([str(record) for record in contact_book.data.values()])
    return contact_list

# Function to add a new contact
@input_error
def handler_add_contact(*args):
    command = " ".join(args)
    _, *args = command.split(maxsplit=3)
    if len(args) < 3:
        return "Give me name, phone, and birthday please"
    name, phone, birthday = args
    record = Record(name, phone, birthday)
    contact_book.add_record(record)
    save_address_book()
    return f"Contact {name} added with phone number {phone} and birthday {birthday}"

# Function to change a contact's phone number
@input_error
def handler_change_phone(*args):
    command = " ".join(args)
    _, name, new_phone = command.split()
    record = contact_book.find(name)
    if record:
        record.edit_phone(record.phones[0].value, new_phone)
        save_address_book()
        return f"Phone number for {name} updated to {new_phone}"
    else:
        return "Contact not found"

# Function to get a contact's phone number
@input_error
def handler_get_phone(*args):
    command = " ".join(args)
    _, name = command.split()
    record = contact_book.find(name)
    if record:
        return f"Phone number for {name}: {record.phones[0].value}"
    else:
        return "Contact not found"

# Function to get a contact's birthday
@input_error
def handler_get_birthday(*args):
    command = " ".join(args)
    _, name = command.split()
    record = contact_book.find(name)
    if record and record.birthday:
        return f"Birthday of {name}: {record.birthday.value}"
    elif record and not record.birthday:
        return f"{name} does not have a birthday recorded."
    else:
        return "Contact not found"

# Function to search for contacts
def handler_search_contacts(query):
    results = []
    for record in contact_book.data.values():
        if query in record.name.value:
            results.append(record)
        for phone in record.phones:
            if query in phone.value:
                results.append(record)
    if results:
        result_str = "Search results:\n" + "\n".join([str(record) for record in results])
        return result_str
    else:
        return "No matching contacts found."


OPERATORS = {
    'hello': handler_greetings,
    'close': handler_bye,
    'exit': handler_bye,
    'show all': handler_show_all_contacts,
    'add contact': handler_add_contact,
    'change phone': handler_change_phone,
    'get phone': handler_get_phone,
    'get birthday': handler_get_birthday,
    'search contact': handler_search_contacts,
}