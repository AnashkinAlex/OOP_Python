class AppVK:
    def __init__(self):
        self.name = 'ВКонтакте'

class AppYouTube:
    def __init__(self, memory_max):
        self.name = 'YouTube'
        self.memory_max = memory_max

class AppPhone:
    def __init__(self, phone_list):
        self.name = 'Phone'
        self.phone_list = phone_list


class SmartPhone:
    def __init__(self, model):
        self.model = model
        self.apps = []

    def add_app(self,app):
        if type(app) not in list(map(lambda x: type(x), self.apps)):
            self.apps.append(app)
        else:
            raise AttributeError

    def remove_app(self, app):
        self.apps.remove(app)

sm = SmartPhone("Honor 1.0")
sm.add_app(AppVK())
sm.add_app(AppYouTube(2048))
sm.add_app(AppYouTube(2048))
for a in sm.apps:
    print(a.name)