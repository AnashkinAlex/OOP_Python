class Product:
    all_id = 1
    def __init__(self, name, weight, price):
        self.id = Product.all_id
        self.price = price
        self.name = name
        self.weight = weight
        Product.all_id += 1

    def __setattr__(self, key, value):
        if key in ['price', 'weight']:
            if type(value) not in [int, float] or  value < 0 :
                raise TypeError("Неверный тип присваиваемых данных.")
        elif key == 'name':
            if not isinstance(value, str)   :
                raise TypeError("Неверный тип присваиваемых данных.")
        return object.__setattr__(self,key,value)

    def __delattr__(self, item):
        if item == 'id':
            raise AttributeError("Атрибут id удалять запрещено.")
        object.__delattr__(self, item)

class Shop:
    def __init__(self, name):
        self.name = name
        self.goods = []

    def add_product(self, product):
        if isinstance(product, Product):
            self.goods.append(product)

    def remove_product(self, product):
        self.goods.remove(product)

shop = Shop("Балакирев и К")
book = Product("Python ООП", 100, 1024)
shop.add_product(book)
shop.add_product(Product("Python", 150, 512))
for p in shop.goods:
    print(f"{p.name}, {p.weight}, {p.price}, {p.id}")