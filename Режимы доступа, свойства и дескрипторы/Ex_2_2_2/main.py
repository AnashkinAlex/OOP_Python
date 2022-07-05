class WindowDlg:
    def __init__(self, title, width, height):
        self.__title = title
        self.__width = width
        self.__height = height

    def show(self):
        print(f'{self.__title}:{self.__width},{self.__height}')

    @staticmethod
    def check_size(size):
        return True if(size >= 0 and size <= 10000 and type(size) in (int, float)) else False

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if WindowDlg.check_size(width) and self.__width != width:
            self.__width = width
            self.show()

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if WindowDlg.check_size(height) and  self.__height != height:
            self.__height = height
            self.show()

a = WindowDlg('Окно 1', 100, 50)
a.width = 1000