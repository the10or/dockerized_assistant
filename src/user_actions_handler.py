from pathlib import Path

from error_handler import input_error
from address_book.contact_book import AddressBook
import globals
from file_config import file_contact_book, file_notes
import pickle
from sort_file import sort
from notes import note_book

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

    
@input_error
def handler_add_note(data):
    
     tags = []
     new_data = data
     for i in data:
         if '#' in i:
             
             tags.append(i)
             
             
     for i in new_data:
         for j in tags:
             if j == i:
                 new_data.remove(i)     

    
     if tags:
         
         
         for i in new_data:
            for j in tags:
                if j == i:
                    new_data.remove(i)
         text = ' '.join(new_data)
     else:
         text = data



     if tags:
        
        n = note_book.Note(text, tags)
        
        globals.note.add_note(n)

        print(f'Note has been added successfully:')
        for i in globals.note.data.values():
            if type(i) == list:
                for j in i:
                    print(str(j))
            print(str(i))


        
        return '>>>'
     
     else:
        n = note_book.Note(text)
        
        globals.note.add_note(n)

        print(f'Note has been added successfully:')
        for i in globals.note.data.values():
            if type(i) == list:
                for j in i:
                    print(str(j))
            print(str(i))
        return '>>>'

@input_error
def handler_add_tag(data):
    globals.note.add_tag(data[1], data[2])
    print(f'Tag has been added successfully:')
    for i in globals.note.data.values():
        if type(i) == list:
            
            for j in i:
                print(str(j))
        print(str(i))
    return '>>>'
    

@input_error    
def handler_edit_title(data):
    globals.note.edit_title(data[0], data[1])
    print(f'Tag has been added successfully:')
    for i in globals.note.data.values():
        if type(i) == list:
            
            for j in i:
                print(str(j))
        print(str(i))
    return '>>>'
  

    
@input_error    
def handler_edit_text(data):
    globals.note.edit_text(data[0], data[1])
    print(f'Tag has been added successfully:')
    for i in globals.note.data.values():
        if type(i) == list:
            print('here')
            for j in i:
                print(str(j))
        print(str(i))
    return '>>>'
    

@input_error 
def handler_sort_note(*args):
    print('Start sorting')
   
    return print(globals.note.sort_note())

@input_error
def handler_find_note(data):
    lst = []
   
    for i in data: 
        lst.append(globals.note.find_note(i))
    return '\n'.join(lst)


@input_error
def handler_delete_note(data):
    for i in data:
        globals.note.delete_note(i)
    print(f'Note(s) has been deleted successfully. Remained notes:')
    for i in globals.note.data.values():
        if type(i) == list:
            for j in i:
                print(str(j))

        print(str(i))
    return '>>>'
        
       






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
    "add contact": handler_add_contact,
    'add note' : handler_add_note,
    'edit note text': handler_edit_text,
    'edit note title': handler_edit_title,
    'sort note': handler_sort_note,
    'find note': handler_find_note,
    'delete note': handler_delete_note,
    'add note tag': handler_add_tag

}
