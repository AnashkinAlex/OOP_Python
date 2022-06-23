TYPE_OS = 1 # 1 - Windows; 2 - Linux

class DialogWindows:
    name_class = "DialogWindows"


class DialogLinux:
    name_class = "DialogLinux"


# здесь объявляйте класс Dialog
class Dialog:
    def __new__(cls, *args, **kwargs):
        object_class = None
        if TYPE_OS == 1:
            object_class = super().__new__(DialogWindows)
        else:
            object_class = super().__new__(DialogLinux)

        object_class.name = args[0]
        return object_class