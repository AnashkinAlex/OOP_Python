class LessonItem:
    attrs = {'title': str, 'practices': int, 'duration': int}
    def __init__(self, title, practices, duration):
        self.title = title
        self.practices = practices
        self.duration = duration

    def __setattr__(self, key, value):
        if key in self.attrs:
            if type(value) != self.attrs[key]:
                raise TypeError("Неверный тип присваиваемых данных.")
            if (key == 'practices' or key == 'duration') and value < 0:
                raise TypeError("Неверный тип присваиваемых данных.")

    def __getattr__(self, item):
        return False

    def __delattr__(self, item):
        if item in ['title', 'practices', 'duration']:
            print('Незя удалять этот атрибут')
        else:
            object.__delattr__(self, item)


class Module:
    def __init__(self, name):
        self.name = name
        self.lessons = []

    def add_lesson(self, lesson):
        if isinstance(lesson, LessonItem):
            self.lessons.append(lesson)
        else:
            print('lesson не объект класса LessonItem')

    def remove_lesson(self,indx):
        self.lessons.pop(indx)

class Course:
    def __init__(self, name):
        self.name = name
        self.modules = []

    def add_module(self, module):
        if isinstance(module, Module):
            self.modules.append(module)
        else:
            print('module не объект класса Module')

    def remove_module(self, indx):
        self.modules.pop(indx)

course = Course("Python ООП")
module_1 = Module("Часть первая")
module_1.add_lesson(LessonItem("awfda", 0, 1000))
module_1.add_lesson(LessonItem("2", 10, 1200))
module_1.add_lesson(LessonItem("Урок 3", 5, 800))
course.add_module(module_1)
module_2 = Module("Часть вторая")
module_2.add_lesson(LessonItem("Урок 1", 7, 1000))
module_2.add_lesson(LessonItem("5", 10, 1200))
course.add_module(module_2)