class CardCheck:
    CHARS_FOR_NAME = ''.join(list(map(lambda x: chr(x),[i for i in range(97, 122)] + [i for i in range(48, 58)]))).upper() + '-' + ' '
    NUMBERS = ''.join(list(map(lambda x: chr(x),[i for i in range(48, 58)]))) + '-'
    @staticmethod
    def check_card_number(number):
        for item in number:
            if item not in CardCheck.NUMBERS:
                return False
        number_card = number.split('-')
        if len(number_card) != 4:
            return False
        else:
            for item in number_card:
                if len(item) != 4:
                    return False
        return True

    @staticmethod
    def check_name(name):
        couter = 0
        for item in name:
            if item not in CardCheck.CHARS_FOR_NAME:
                return False

            if item == ' ':
                couter += 1
        if couter == 1:
            return True
        else:
            return False





is_number = CardCheck.check_card_number("123А-5678-9012-0000")
is_name = CardCheck.check_name("SERGEI BALAKIREV")
print(is_name,'   ', is_number)


print(CardCheck.CHARS_FOR_NAME)

