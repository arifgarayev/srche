from datetime import datetime, timedelta


def x():
    return 1


class MyBaseClass:
    def __init__(self):
        self.num = x()
        self.y = 2


class MyDerivedClass(MyBaseClass):
    def __init__(self):
        super().__init__()

        # self.num = 4

    def pprint(self):
        print(self.num)

    def complete_query(self, f):
        def wrapper(*args, **kwargs):
            return f(*args, **kwargs)

        return wrapper


if __name__ == "__main__":
    print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
