from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    def __init__(self, value):
        if not value:
            raise ValueError("Ім\'я обов\'язкове")
        super().__init__(value)

class Phone(Field):
    def __init__(self, value):
        if not self._validate_phone(value):
            raise ValueError("Неправильний формат номера")
        super().__init__(value)

    def _validate_phone(self, value):
        return len(value) == 10 and value.isdigit()



class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        
    def return_name(self):
        return self.name

    def add_phone(self, phone):
            self.phones.append(Phone(phone))


    def remove_phone(self, phone):
        self.phones = [p for p in self.phones if p.value != phone]
    
    def edit_phone(self, old_num, new_num):
        self.find_phone(old_num)
        self.add_phone(new_num)
        self.remove_phone(old_num)
    
    def find_phone(self,number):
         for phone in self.phones:
              if phone.value == number:
                   return phone 
              else: raise ValueError ("Такого номера не існує")

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    def add_record(self, record:Record):
          self.data[record.name.value] = record

    def find(self, name):
         return self.data.get(name)
    
    def delete(self, name):
         if name in self.data:
              del self.data[name]
    
    def __str__(self):
        return "\n".join(str(record) for record in self.data.values())


    
# Створення нової адресної книги
book = AddressBook()
# Створення запису для John
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")

    # Додавання запису John до адресної книги
book.add_record(john_record)

    # Створення та додавання нового запису для Jane
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

    # Виведення всіх записів у книзі
for name, record in book.data.items():
    print(record)

    # Знаходження та редагування телефону для John
john = book.find("John")
john.edit_phone("1234567890", "1112223333")

print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

    # Пошук конкретного телефону у записі John
found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")  # Виведення: 5555555555
    # Видалення запису Jane
book.delete("Jane")





