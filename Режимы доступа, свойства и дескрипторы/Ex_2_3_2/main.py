class ValidateString:
    def __init__(self, min_length=3, max_length=100):
        self.min_length = min_length
        self.max_length = max_length
    def validate(self, string):
        if type(string) == str and self.min_length <= len(string) <= self.max_length:
            return True

        else:
            return False

class StringValue:
    def __init__(self, validator):
        self.validator = validator

    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if self.validator.validate(value):
            instance.__dict__[self.name] = value

class RegisterForm:
    login = StringValue(validator= ValidateString())
    password = StringValue(validator= ValidateString())
    email = StringValue(validator= ValidateString())

    def __init__(self, login, password, email):
        self.email = email
        self.password = password
        self.login = login

    def get_fields(self):
        return [self.login, self.password, self.email]

    def show(self):
        print(
            '<form>\n'
            f'Логин:{self.login}\n'
            f'Пароль:{self.password}\n'
            f'Email:{self.email}\n'
            '</form>\n'
        )
rf = RegisterForm('Bo00', 'FooBar', 'BuzFuz')
print(rf.__dict__)
rf.show()
print(rf.get_fields())
rf = RegisterForm('B0', 42, 'BuzFuz')
print(rf.__dict__)

