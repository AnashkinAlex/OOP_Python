class Item:
    def __init__(self, name, money):
        self.name = name
        self.money = money

    def __add__(self, other):
        return self.money + other.money

    def __radd__(self, other):
        return other + self.money

class Budget:
    def __init__(self):
        self.budget_list = []

    def add_item(self,it):
        self.budget_list.append(it)

    def remove_item(self, indx):
        self.budget_list.pop(indx)

    def get_items(self):
        return self.budget_list

my_budget = Budget()
my_budget.add_item(Item("Курс по Python ООП", 2000))
my_budget.add_item(Item("Курс по Django", 5000.01))
my_budget.add_item(Item("Курс по NumPy", 0))
my_budget.add_item(Item("Курс по C++", 1500.10))
my_budget.remove_item(0)
s = 0
for x in my_budget.get_items():
    s = s + x
print(s)
