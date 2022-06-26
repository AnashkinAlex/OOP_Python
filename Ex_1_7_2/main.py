class FormLogin:
    def __init__(self, lgn, psw):
        self.login = lgn
        self.password = psw

    def render_template(self):
        return "\n".join(['<form action="#">', self.login.get_html(), self.password.get_html(), '</form>'])

class TextInput:
    CHARS = "абвгдеёжзийклмнопрстуфхцчшщьыъэюя "
    ascii = list(map(lambda x: chr(x),[i for i in range(65, 91)] + [i for i in range(97, 122)] + [i for i in range(48, 58)]))
    CHARS_CORRECT = CHARS + CHARS.upper() + ''.join(ascii)

    def __init__(self,name, size=10):
        self.check_name(name)
        self.name = name
        self.size = size

    def get_html(self):
        return f"<p class='login'>{self.name}: <input type='text' size={self.size} />"

    @classmethod
    def check_name(cls, name):
        for item in name:
            if item not in cls.CHARS_CORRECT:
                raise ValueError('некорректное имя поля')

        if type(name) != str or len(name) < 3 or len(name) > 50:
            raise ValueError('некорректное имя поля')

        return True


class PasswordInput:
        CHARS = "абвгдеёжзийклмнопрстуфхцчшщьыъэюя "
        ascii = list(map(lambda x: chr(x),[i for i in range(65, 91)] + [i for i in range(97, 122)] + [i for i in range(48, 58)]))
        CHARS_CORRECT = CHARS + CHARS.upper() + ''.join(ascii)

        def __init__(self, name, size=10):
            self.check_name(name)
            self.name = name
            self.size = size

        def get_html(self):
            return f"<p class='password'>{self.name}: <input type='text' size={self.size} />"
        @classmethod
        def check_name(cls, name):
            for item in name:
                if item not in cls.CHARS_CORRECT:
                    raise ValueError('некорректное имя поля')

            if type(name) != str or len(name) < 3 or len(name) > 50:
                raise ValueError('некорректное имя поля')

            return True


login = FormLogin(TextInput("Лог"), PasswordInput("Пар"))
html = login.render_template()
