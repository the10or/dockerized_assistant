# Personal Assistant

---

[Personal Assistant](ttps://github.com/dry_kiss.py/personal_assistant.git) is a Python application that can maintain an address book with names of contacts,<br> their phone numbers and birthday dates, take notes, and organise files on your hard drive by corresponding content category. <br>
The application is created by the dry_kiss.py team<br> and uses a command line interface.

---

## Requirements.
To run the application, you need to have Python 3 on your computer.

---

## Installation.

To install the app, download the repository from GitHub: 

`git clone https://github.com/dry_kiss.py/personal_assistant.git`

Go to the project directory and run the installation as follows:
`pip install -e . `

To ensure that the program has been successfully installed on your system, use  
`pip show personal-assistant` 
command.

---

## Launching the app
If the application is successfully installed, you can run it on the command line
from anywhere in your operating system<br> using
`start-bot` command.
You will be prompted to enter the command you want.
If you are not sure which command<br> you actually need, type "help".
A list of available commands will be displayed. 

---

## Availible commands

| Command                                                                       | Action                                                                                                                                                     |
|-------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **hello** / **hi**                                                            | nothing special, just ordinary greeting message                                                                                                            |
| **help**                                                                          | displays the list of availible commands                                                                                                                    |
| **add note** [ _text_ ]                                                       | adds a note with the corresponding text                                                                                                                    |
| **add note tag** [ _text_ ] [ _#tag_ ]                                        | adds a tag to the note with corresponding text                                                                                                             |
| **edit notetext** [ _text_ ] [ _new text_ ]                                   | edits the text of the note                                                                                                                                 |                 
| **edit notetitle** [ _#tag_ ] [ _#new tag_ ]                                  | edits the header of the note(the first tag)                                                                                                                |
| **sort note**                                                                 | sorts notes alphabetically                                                                                                                                 |
| **find note** [ _text / #tag_ ]                                               | searches for the note by text or tag                                                                                                                       |
| **delete note** [ _text / #tag_ ]                                             | deletes the note                                                                                                                                           |
 | **sort dir** [ _Path to the folder_ ]                                         | sorts the files in the specified folder and places them in subfolders according to the appropriate content categories                                      |
| **add contac**t [ _firstname_ ] [ _lastname_ ]                                | adds the contact with corresponding name and lastname  to the address book                                                                                 |
| **add contact** [ _firstname_ ]                                               | adds the contact to the address book with the name only                                                                                                    |
| **add phone** [ _name_ ] [ _phone_ ]                                          | adds the contact with name and phone to the address book, the phone number must be 8 or 10 digits long                                                     |
| **change birthday** [_name_] [_new birthday_ (in format xx/xx/xxxx)]            | changes the birthday date                                                                                                                                  |
| **search contacts** [ ... ]                                                   | searches for contacts in the address book and displays the resulting list if the search is successful,<br> otherwise displays the "Nothing found" notification |
| **find contact** [_name_] or  **find contact** [_first name_] [_second name_] | searches for a contact by name or by first and last name                                                                                                   |
| **delete contact** [__name__]                                                 | deletes the contact by the given name                                                                                                                      |
| **close** / **exit** / **good bye**                                           | terminates the application                                                                                                                                 |
___
## Authors
the DRY_KISS.py team
___
## License
This program is distributed under the MIT License. See the LICENSE file for details.
___
