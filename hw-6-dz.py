from collections import UserDict
from dis import findlabels


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    def __init__(self, name):
        super().__init__(name)

class Phone(Field):
    def __init__(self, phone):
        if len(phone) < 10:
            raise ValueError('Phone is too short')
        elif len(phone) > 10:
            raise ValueError('Phone is too long')
        elif not phone.isdigit():
            raise ValueError('Please write correct number, only numbers')
        super().__init__(phone)


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def find_phone(self, phone_find: str):
        for phone in self.phones:
            if phone.value == phone_find:
                return phone

    def add_phone(self, phone):
        phone_obj = Phone(phone)
        self.phones.append(phone_obj)


    def show_phones(self):
        return [phone.value for phone in self.phones]

    def remove_phone(self, phone):
        phone_deleted = self.find_phone(phone)
        if phone_deleted:
            self.phones.remove(phone_deleted)
        else:
            print(f"don't find number {phone} in {self.show_phones()}")

    def edit_phone(self, old_numb: str, new_numb: str)-> None:
        if not self.find_phone(new_numb):
            if old_numb == new_numb:
               print('Please write a new number different from the old one')
            if self.find_phone(old_numb):
                self.phones[self.phones.index(self.find_phone(old_numb))] = Phone(new_numb)
                print(f"Number {old_numb} successfully changed to {new_numb}")
            else:
               raise  ValueError(f"Can't find number {old_numb} in {self.show_phones()}")
        else:
            print(f'Number "{old_numb}" was added previously')

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):
    def add_record(self, record) -> None:
        self.data[record.name.value] = record

    def find(self, name: str):
        if name in self.data:
            return self.data.get(name)
        else:
            raise ValueError('Name not found')

    def delete(self, name: str)->None:
        if self.find(name):
            self.data.pop(name)
            print(f"Name '{name}' deleted successfully.")
        else:
            raise ValueError(f"Name '{name}' not found.")

    def __str__(self):
        return (f'\n=========Address book contacts========== \n'
                + f'\n'.join(str(record) for record in self.data.values())) +'\n'




print("_________________Test_____________________")
#__init__
john_record = Record('John')
daria_record = Record('Daria')
vlados_record = Record('Vlados')
#__add_phone__
john_record.add_phone('1234567891')
vlados_record.add_phone('1234567892')
daria_record.add_phone('1234567893')
# output
book = AddressBook()
book.add_record(john_record)
book.add_record(daria_record)
book.add_record(vlados_record)
print(book)
#delete
book.delete('John')
print(book)
#find
vlad = book.find("Vlados")
vlad.edit_phone('1234567892', '5555555555')
vlados_record.add_phone('1111111111')
vlad.edit_phone('1111111111', '5555555555')
print(book)
print(vlad)


