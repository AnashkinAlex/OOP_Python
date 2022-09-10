class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

class Lib:
    def __init__(self):
        self.book_list = []


    def __add__(self, other):
        self.book_list.append(other)

        return self

    def __sub__(self, other):
        if isinstance(other, Book):
            self.book_list.remove(other)
        elif isinstance(other, int):
            self.book_list.pop(other)
        else:
            raise ValueError('Параметр для удаления либо Book, либо int, иначе иди нахуй')
        return self

    def __len__(self):
        return len(self.book_list)

lib_1 = Lib()
print(lib_1)

lib_1 += Book('Горе от ума','None',1985)
lib_1 += Book('Просто делай, делай просто','None',2017)
book_1 = Book('Делай хорошо, иначе нахуй надо!','Анашкин Алексей Григорьевич', 2022)
lib_1 += book_1
print(lib_1.book_list)
lib_1 -= book_1
print(lib_1.book_list)






