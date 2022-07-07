class TreeObj:
    def __init__(self, indx, value = None):
        self.indx = indx
        self.value = value
        self.__left = self.__right = None

    @property
    def left(self):
        return self.__left

    @left.setter
    def left(self, left):
        self.__left = left

    @property
    def right(self):
        return self.__right

    @right.setter
    def right(self, right):
        self.__right = right



class DecisionTree:
    @classmethod
    def add_obj(cls, obj, node = None, left = True):
        if node is not None:
            if left:
                node.left = obj
            else:
                node.right = obj
        return obj

    @classmethod
    def predict(cls, root, x):
        last_obj = root
        while last_obj:
            tmp = cls.get_next(last_obj, x)
            if tmp is None:
                break

            last_obj = tmp
        return last_obj.value

    @classmethod
    def get_next(cls, obj,x ):
        if x[obj.indx] == 1:
            return obj.left
        return obj.right

root = DecisionTree.add_obj(TreeObj(0))
v_11 = DecisionTree.add_obj(TreeObj(1), root)
v_12 = DecisionTree.add_obj(TreeObj(2), root, False)
DecisionTree.add_obj(TreeObj(-1, "будет программистом"), v_11)
DecisionTree.add_obj(TreeObj(-1, "будет кодером"), v_11, False)
DecisionTree.add_obj(TreeObj(-1, "не все потеряно"), v_12)
DecisionTree.add_obj(TreeObj(-1, "безнадежен"), v_12, False)

x = [1, 1, 0]
res = DecisionTree.predict(root, x) # будет программистом
print(res)
