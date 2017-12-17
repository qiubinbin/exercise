from abc import ABCMeta, abstractclassmethod, abstractmethod


class Test(metaclass=ABCMeta):
    @abstractmethod
    def push(self, item):
        pass

    @abstractmethod
    def pop(self):
        pass

    @abstractclassmethod
    def pp(cls):
        pass

    @property
    @abstractmethod
    def size(self):
        pass


class Test1(Test):
    """chifan"""

    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    @classmethod
    def pp(cls):
        print('test')


class Test2(Test1):
    @property
    def size(self):
        return len(self.items)


s = Test2()
s.push(5)
print(s.pop())
Test2.pp()
