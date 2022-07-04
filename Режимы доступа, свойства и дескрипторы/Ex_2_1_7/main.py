from random import  randint


class EmailValidator:
    def __new__(cls, *args, **kwargs):
        return None

    @classmethod
    def get_random_email(cls):
        lst_ascii = [item for item in range(48,58)] + [i for i in range(65,91)] + [i for i in range(97,123)]
        lst_ascii = list(map(lambda x: chr(x),lst_ascii)) + ['_']
        email = ''

        for item in range(randint(10,100)):
            email += lst_ascii[randint(0,len(lst_ascii)-1)]
        email += '@'
        for item in range(randint(5,30)):
            email += lst_ascii[randint(0,len(lst_ascii)-1)]

        email += '.'
        for item in range(randint(2,5)):
            email += lst_ascii[randint(0, len(lst_ascii))]

        return email

    @classmethod
    def check_email(cls, email):
        lst_ascii = [item for item in range(48, 58)] + [i for i in range(65, 91)] + [i for i in range(97, 123)]
        lst_ascii = list(map(lambda x: chr(x), lst_ascii)) + ['_', '@', '.']
        if not cls.__is_email_str(email):
            return False

        two_pieces_emal = email.split('@')
        if len(two_pieces_emal[0]) > 100 or len(two_pieces_emal[0]) == 0:
            return False

        if len(two_pieces_emal[1]) > 50 or len(two_pieces_emal[1]) == 0:
            return False

        if '@' not in email:
            return False

        counter = 0
        for item in email:
            if item == "@":
                counter += 1
        if counter > 1:
            return False


        if email.count('..') > 0:
            return False

        if '.' not in two_pieces_emal[1]:
            return False

        for item in email:
            if item not in lst_ascii:
                return False

        return True


    @staticmethod
    def __is_email_str(email):
        return True if(isinstance(email, str)) else False



print(EmailValidator.check_email("sc..lib@list.ru"))
