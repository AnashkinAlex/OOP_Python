class Dimensions:
    MIN_DIMENSIONS = 10
    MAX_DIMENSIONS = 10000

    def __init__(self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c

    @classmethod
    def check_value(cls, value):
        if isinstance(value, (int, float)) and  cls.MIN_DIMENSIONS <= value <= cls.MAX_DIMENSIONS:
            return  True
        return False

    @property
    def a(self):
        return self.__a

    @a.setter
    def a(self, value):
        if self.check_value(value):
            self.__a = value

    @property
    def b(self):
        return self.__b

    @b.setter
    def b(self, value):
        if self.check_value(value):
            self.__b = value

    @property
    def c(self):
        return self.__c

    @c.setter
    def c(self, value):
        if self.check_value(value):
            self.__c = value

    def get_volume(self):
        return self.__a * self.__b * self.__c

    def __ge__(self, other):
        return self.get_volume() >= other.get_volume()

    def __le__(self, other):
        return self.get_volume() <= other.get_volume()

    def __lt__(self, other):
        return self.get_volume() < other.get_volume()

    def __gt__(self, other):
        return self.get_volume() > other.get_volume()

class ShopItem:
    def __init__(self, name, price, dim):
        self.name = name if type(name) is str else None
        self.price = price if isinstance(price, (int, float)) else None
        self.dim = dim if isinstance(dim, Dimensions) else None


trainers = ShopItem('кеды', 1024, Dimensions(40, 30, 120))
umbrella = ShopItem('зонт', 500.24, Dimensions(10, 20, 50))
fridge = ShopItem('холодильник', 40000, Dimensions(2000, 600, 500))
chair = ShopItem('табуретка', 2000.99, Dimensions(500, 200, 200))
lst_shop = [trainers, umbrella, fridge, chair]
lst_shop_sorted = sorted(lst_shop, key=lambda x: x.dim)
for item in lst_shop_sorted:
    print(item.name)

