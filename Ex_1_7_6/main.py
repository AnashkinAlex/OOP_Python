class Message:
    def __init__(self, text):
        self.text = text
        self.fl_like = False


class Viber:
    lst_message = []

    @classmethod
    def add_message(cls, msg):
        cls.lst_message.append(msg)

    @classmethod
    def remove_message(cls, msg):
        cls.lst_message.remove(msg)

    @classmethod
    def set_like(cls, msg):
        if msg.fl_like == True:
            msg.fl_like = False
        else:
            msg.fl_like = True

    @classmethod
    def show_last_message(cls, quantity):
        for i in range(quantity):
            print(cls.lst_message[i].text)

    @classmethod
    def total_messages(cls):
        return len(cls.lst_message)


msg = Message("Всем привет!")
Viber.add_message(msg)
Viber.add_message(Message("Это курс по Python ООП."))
Viber.add_message(Message("Что вы о нем думаете?"))
Viber.set_like(msg)
Viber.remove_message(msg)
Viber.show_last_message(2)
