class DocMeta(type):
    def __init__(self, name, base, dict):
        for key, value in dict.items():
            if key.startswith('__'): continue
            if not hasattr(value, '__call__'): continue
            if not getattr(value, '__doc__'):
                raise TypeError
        type.__init__(self, name, base, dict)


class Foo(metaclass=DocMeta):
    s = 5

    def __init__(self):
        self.a = 7

    def spam(self, a, b):
        '''Spam do nothing!'''
        print('Spam do nothing!')


b = Foo()
print(Foo.__dict__)
