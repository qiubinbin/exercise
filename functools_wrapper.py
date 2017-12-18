def wrap(func):
    """装饰器"""

    def call_it(*args, **kwargs):
        print('开始调用')
        return func(*args, **kwargs)

    return call_it


@wrap
def hello():
    """say hello"""
    print('hello world')


hello()
print(hello.__doc__)
print(hello.__name__)
print(hello.__module__)

from functools import update_wrapper


def wrap1(func):
    """装饰器"""

    def call_it(*args, **kwargs):
        print('开始调用')
        return func(*args, **kwargs)

    return update_wrapper(call_it, func)


@wrap1
def hello1():
    """say hello"""
    print('hello world')
hello1()
print(hello1.__doc__)
print(hello1.__name__)
print(hello1.__module__)
