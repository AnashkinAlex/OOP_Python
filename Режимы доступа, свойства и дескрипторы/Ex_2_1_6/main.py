class ObjList:

    def __init__(self, data):
        self.__data = data
        self.__next = None
        self.__prev = None

    def set_next(self, obj):
        self.__next = obj

    def set_prev(self, obj):
        self.__prev = obj

    def get_next(self):
        return self.__next

    def get_prev(self):
        return self.__prev

    def set_data(self, data):
        self.__data = data

    def get_data(self):
        return self.__data



class LinkedList:
    def __init__(self, head = None, tail = None):
        self.lst = []
        self.head = head
        self.tail = tail

    def add_obj(self, obj):
        if self.tail:
            self.tail.set_next(obj)
        obj.set_prev(self.tail)

        self.tail = obj
        if not self.head:
            self.head = obj

    def remove(self):
        if self.tail is None:
            return

        tmp = self.tail.get_prev
        if tmp:
            tmp.set_next(None)

        self.tail = tmp
        if self.tail is None:
            self.head = None

    def get_data(self):
        lst = []
        head = self.head
        while head:
            lst.append(head.get_data())
            head = head.get_next()
        return lst


lst = LinkedList()
lst.add_obj(ObjList("данные 1"))
lst.add_obj(ObjList("данные 2"))
lst.add_obj(ObjList("данные 3"))
res = lst.get_data()    # ['данные 1', 'данные 2', 'данные 3']

print(res)

