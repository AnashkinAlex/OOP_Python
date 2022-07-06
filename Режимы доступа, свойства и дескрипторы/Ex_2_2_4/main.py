class RadiusVector2D:
    MIN_COORD = -100
    MAX_COORD = 1024

    def __init__(self, x=0, y=0):
        self.__x = self.__y = 0
        if RadiusVector2D.check_value(x):
            self.__x = x

        if RadiusVector2D.check_value(y):
            self.__y = y


    @classmethod
    def check_value(cls,value):
        return type(value) in (int,float) and  cls.MIN_COORD <= value <= cls.MAX_COORD

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value_x):
        if RadiusVector2D.check_value(value_x):
            self.__x = value_x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value_y):
        if RadiusVector2D.check_value(value_y):
            self.__y = value_y


    @staticmethod
    def norm2(vector):
        return vector.x**2 + vector.y**2



r5 = RadiusVector2D(-102, 2000)
print(r5.x , r5.y)