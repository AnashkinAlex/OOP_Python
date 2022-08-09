class PhoneNumber:
    def __init__(self, number, fio):
        self.number = number
        self.fio = fio


class PhoneBook:
    def __init__(self):
        self.dictionary = []

    def add_phone(self, phone):
         self.dictionary.append(phone)

    def remove_phone(self,indx):
        self.dictionary.pop(indx)

    def get_phone_list(self):
        return self.dictionary

p = PhoneBook()
p.add_phone(PhoneNumber(12345678901, "Сергей Балакирев"))
p.add_phone(PhoneNumber(21345678901, "Панда"))
phones = p.get_phone_list()
print(phones)
