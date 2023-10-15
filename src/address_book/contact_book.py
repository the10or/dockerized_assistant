from collections import UserDict
from datetime import datetime,timedelta
import pickle
from src.record import Record


class AddressBook(UserDict):
    def __init__(self):
        self.data = {}

    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        if name in self.data:
            del self.data[name]

    def iterator(self, N=1):
        records = list(self.data.values())
        for i in range(0, len(records), N):
            yield records[i:i + N]

    def save_to_file(self, file_path):
        with open(file_path, 'wb') as file:
            pickle.dump(self.data, file)

    
    def load_from_file(self, file_path):
        try:
            with open(file_path, 'rb') as file:
                self.data = pickle.load(file)
        except FileNotFoundError:
            pass

    def search(self, query):
        results = []
        for record in self.data.values():
            if query in record.name.value:
                results.append(record)
            for phone in record.phones:
                if query in phone.value:
                    results.append(record)
        return results

