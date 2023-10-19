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

## Available commands

| Command                                                                       | Action                                                                                                                                                       |
|-------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **hello** / **hi**                                                            | nothing special, just ordinary greeting message                                                                                                              |
| **help**                                                                      | display the list of availible commands                                                                                                                       |
| **add note** [ _title_ ]                                                      | add a note with the corresponding title                                                                                                                      |
| **add tags** [ _title_ ] [ _#tag1_ ] [ _#tag2_ ] ...                          | add tag/tags to the note with corresponding title                                                                                                            |
| **edit note_text** [ _title_ ] [ _text_ ]                                     | add/edit the text of the note                                                                                                                                |                 
| **find note** [ _#title_ ]                                                    | find note with corresponding title                                                                                                                           |
| **delete note** [ _#title_ ]                                                  | delete note with corresponding title                                                                                                                         |
| **list notes**                                                                | sort(alphabetically ) and show list of notes                                                                                                                 |
| **sort dir** [ _Path to the folder_ ]                                         | sort the files in the specified folder and places them in subfolders according to the appropriate content categories                                         |
| **add contact**t [ _firstname_ ] [ _lastname_ ]                               | add the contact with corresponding name and lastname  to the address book                                                                                    |
| **add contact** [ _firstname_ ]                                               | add the contact to the address book with the name only                                                                                                       |
| **add phone** [ _name_ ] [ _phone_ ]                                          | add the contact with name and phone to the address book, the phone number must be 8 or 10 digits long                                                        |
| **show all**                                                                  | show all contact list from address book                                                                                                                      |
| **change birthday** [_name_] [_new birthday_ (in format xx/xx/xxxx)]          | add/change the birthday date                                                                                                                                 |
| **search contacts** [ ... ]  ?                                                | search for contacts in the address book and displays the resulting list if the search is successful,<br> otherwise displays the "Nothing found" notification |
| **find contact** [_name_] or  **find contact** [_first name_] [_second name_] | search for a contact by name or by first and last name                                                                                                       |
| **delete contact** [__name__]                                                 | delete the contact by the given name                                                                                                                         |
| **close** / **exit** / **good bye**                                           | terminate the application                                                                                                                                    |
___
## Authors
the DRY_KISS.py team
___
## License
This program is distributed under the MIT License. See the LICENSE file for details.
___
