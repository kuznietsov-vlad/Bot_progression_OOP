from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    def __init__(self, name):
        self.name = name


class Phone(Field):
    def __init__(self, phone):
        if len(phone) < 10:
            raise ValueError('Phone is too short')
        elif len(phone) > 10:
            raise ValueError('Phone is too long')
        self.phone = phone


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def find_phone(self, phone_find: str):
        for phone in self.phones:
            if phone.phone == phone_find:
                return phone

    def add_phone(self, phone):
        if phone.isdigit():
            phone_obj = Phone(phone)
            self.phones.append(phone_obj)
        else:
            print('Write correct phone please: ')

    def show_phones(self):
        return [phone.phone for phone in self.phones]

    def delete_phone(self, phone):
        phone_deleted = self.find_phone(phone)
        if phone_deleted:
            self.phones.remove(phone_deleted)
        else:
            print(f"don't find number {phone} in {self.show_phones()}")

    def show_phones(self):
        return [phone.phone for phone in self.phones]

    def edit_phone(self, old_numb: str, new_numb: str):
        if not (old_numb.isdigit() and new_numb.isdigit()):
            raise ValueError(f"Can't find number {old_numb} in {self.show_phones()}")

        if old_numb == new_numb:
            print('Please write a new number different from the old one')


        old_phone_find = self.find_phone(old_numb)

        if old_phone_find:
            self.phones[self.phones.index(old_phone_find)] = Phone(new_numb)
            print(f"Number {old_numb} successfully changed to {new_numb}")
        else:
            print(f"Can't find number {old_numb} in {self.show_phones()}")

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):
    # реалізація класу
    pass

try:
    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("1234567891")
    john_record.add_phone("1234567892")
    print(john_record.show_phones())
    john_record.delete_phone("1234567890")
    print(john_record.show_phones())
    john_record.edit_phone("1234567891", "12334567894")
    #john_record.edit_phone("3234567890", "3234567a890")
    print(john_record.show_phones())
except ValueError:
    print('Please write correct number')
