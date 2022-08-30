class ObjList:
    def __init__(self, data):
        self.__data = data
        self.__prev = None  # предыдущий объект
        self.__next = None  # следующий объект

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data

    @property
    def prev(self):
        return self.__prev

    @prev.setter
    def prev(self, prev):
        self.__prev = prev

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, next):
        self.__next = next


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_obj(self, obj):
        if self.head == None:
            self.head = obj
            self.tail = obj
        else:
            obj.prev = self.tail
            self.tail.next = obj
            self.tail = obj

    def get_indx_obj(self, indx):
        first = self.head
        counter = 0
        while first and counter != indx:
            counter += 1
            first = first.next

        return first

    def remove_obj(self, indx):
        obj = self.get_indx_obj(indx)
        if obj is None:
            return

        p,n = obj.prev, obj.next

        if p:
            p.next = n

        if n:
            n.prev = p

        if self.head == obj:
            self.head = n

        if self.tail == obj:
            self.tail = p

    def __len__(self):
        obj = self.head
        counter = 1
        while obj.next != None:
            counter += 1
            obj = obj.next
        return counter

    def __call__(self, indx, *args, **kwargs):
        obj = self.get_indx_obj(indx)
        return obj.data if obj else None



linked_lst = LinkedList()
linked_lst.add_obj(ObjList("Sergey"))
linked_lst.add_obj(ObjList("Balakirev"))
linked_lst.add_obj(ObjList("Python"))
linked_lst.remove_obj(2)
linked_lst.add_obj(ObjList("Python ООП"))
n = len(linked_lst)  # n = 3
s = linked_lst(1) # s = Balakirev
print(n)
print(s)
print(linked_lst(10))
