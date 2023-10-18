from collections import UserDict
from record import Record
from file_config import file_contact_book
import pickle


class AddressBook(UserDict):
    def __init__(self):
        try:
            with open(file_contact_book, "rb") as f:
                fr = f.read()
                if fr:
                    data = pickle.loads(fr)
                    self.data = data
                else:
                    self.data = {}
        except FileNotFoundError:
            self.data = {}

    def __repr__(self) -> str:
        out = ""
        for name in self:
            d = self.data.get(name, None)
            out += f"{d}\n"
        return out

    def add_record(self, record: set):
        new_user = Record(record)
        self.data.update({new_user.name.value: new_user})
        return f"Sucsessfully added new contact:\n{new_user}"

    def find(self, name: str) -> Record:
        return self.data.get(name, None)

    def find_all(self, input: str) -> list:
        input = input.lower()
        find_result = []
        for contact in self.data.values():
            if input in str(contact.name).lower() and contact.name not in find_result:
                find_result.append(contact.name)
            for single_phone in contact.phones:
                if input in str(single_phone) and contact.name not in find_result:
                    find_result.append(contact.name)
        return find_result

    def delete(self, name:str):
        if self.data.get(name, None):
            del self.data[name]
        else:
            print("unsucsessfull")
            return


    def iterator(self, n=5):
        counter = 0
        output = {}
        for key, value in self.data.items():
            counter += 1
            # print(key)
            # print(f"IF {counter} == {len(self.data)}")
            if counter % n or counter == 0 or counter == len(self.data):
                output.update({key: value})
                if counter == len(self.data):
                    yield output
            else:
                output.update({key: value})
                yield output
                output = {}