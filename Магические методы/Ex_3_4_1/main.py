class NewList:
    def __init__(self, lst = None):
        self.lst = [] if lst == None else lst

    @staticmethod
    def bool_in_str(x):
        if type(x) is bool:
            return str(x)
        else:
            return x

    @staticmethod
    def str_in_bool(x):
        if x == 'True':
            return True
        elif x == 'False':
            return False
        else:
            return x

    def __sub__(self, other):
        if isinstance(other,NewList):
            lst_main = list(map( NewList.bool_in_str,self.lst))
            other_list = list(map( NewList.bool_in_str,other.lst))
            result = []
            for item  in lst_main:
                if item not in other_list:
                    result.append(item)
                else:
                    other_list.remove(item)
        else:
            lst_main = list(map(NewList.bool_in_str, self.lst))
            other_list = list(map(NewList.bool_in_str, other))
            result = []
            for item in lst_main:
                if item not in other_list:
                    result.append(item)
                else:
                    other_list.remove(item)

        return NewList(list(map(NewList.str_in_bool,result)))

    def __rsub__(self, other):
        if isinstance(other,NewList):
            lst_main = list(map( NewList.bool_in_str,self.lst))
            other_list = list(map( NewList.bool_in_str,other.lst))
            result = []
            for item  in other_list:
                if item not in lst_main:
                    result.append(item)
                else:
                    lst_main.remove(item)
        else:
            lst_main = list(map(NewList.bool_in_str, self.lst))
            other_list = list(map(NewList.bool_in_str, other))
            result = []
            for item in other_list:
                if item not in lst_main:
                    result.append(item)

                else:
                    lst_main.remove(item)
        return NewList(list(map(NewList.str_in_bool,result)))
    def get_list(self):
        return self.lst

lst1 = NewList([1, 2, -4, 6, 10, 11, 15, False, True])
lst2 = NewList([0, 1, 2, 3, True])
res_1 = lst1 - lst2 # NewList: [-4, 6, 10, 11, 15, False]
print(res_1.lst)
lst1 -= lst2 # NewList: [-4, 6, 10, 11, 15, False]
print(lst1.lst)
res_2 = lst2 - [0, True] # NewList: [1, 2, 3]
print(res_2.lst)
res_3 = [1, 2, 3, 4.5] - res_2 # NewList: [4.5]
print(res_3.lst)
a = NewList([2, 3])
res_4 = [1, 2, 2, 3] - a # NewList: [1, 2]
print(res_4.lst)