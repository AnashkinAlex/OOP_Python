class Clock:
    __time = 0
    @classmethod
    def __check_time(cls,tm):
        return True if(tm >= 0 and tm < 100000 and type(tm) == int) else False

    def set_time(self,tm):
        if Clock.__check_time(tm):
            Clock.__time = tm

    def get_time(self):
        return Clock.__time

clock = Clock()
clock.set_time(4530)
print(clock.get_time())