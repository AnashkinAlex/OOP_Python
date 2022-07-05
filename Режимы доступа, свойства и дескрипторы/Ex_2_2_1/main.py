class Car:
    def __init__(self):
        self.__model = None

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, model):
        if Car.check_model(model):
            self.__model = model

    @classmethod
    def check_model(cls, model):
        return True if(isinstance(model,str) and len(model)>= 2 and len(model) <= 100) else False


car = Car()
car.model = 'BMW'
car.model = 5
print(car.__dict__)