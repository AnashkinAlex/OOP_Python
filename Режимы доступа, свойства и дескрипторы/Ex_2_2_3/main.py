class StackObj:
    def __init__(self,data):
        self.__next = None
        self.__data = data

    @staticmethod
    def check_next(obj):
        return True if(type(obj) == StackObj or obj == None) else False

    @property
    def next(self):
        return self.__next

    @property
    def data(self):
        return self.__data

    @next.setter
    def next(self, next):
        if StackObj.check_next(next):
            self.__next = next

    @data.setter
    def data(self, data):
        if isinstance(data, str):
            self.__data = data
        else:
            raise TypeError ('Недопустимый тип данных')


class Stack:
    def __init__(self):
        self.top = None
        self.last = None


    def push(self, obj):
        if self.top is None:
            self.top = obj
            obj.next = None
            self.last = obj

        else:
            if self.top.next is None:
                self.top.next = obj
                self.last = obj
            else:
                tmp = self.top
                last_obj = tmp
                while tmp is not None:
                    last_obj = tmp
                    tmp = tmp.next
                last_obj.next = obj
                self.last = obj

    def pop(self):
        tmp = self.top
        if tmp is None:
            return

        while tmp and tmp.next != self.last:
            tmp = tmp.next

        if tmp:
            tmp.next = None

        last = self.last
        self.last = tmp
        if self.last is None:
            self.top = None

        return last

    def get_data(self):
        tmp_lst = []
        tmp = self.top
        while tmp is not None:
            tmp_lst.append(tmp.data)
            tmp = tmp.next
        return tmp_lst



st = Stack()
st.push(StackObj("obj1"))
st.push(StackObj("obj2"))
st.push(StackObj("obj3"))
st.pop()
res = st.get_data()    # ['obj1', 'obj2']
print(res)