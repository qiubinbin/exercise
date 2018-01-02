import collections

a = map(lambda x, y: x + y, [1, 2, -3, 4, - 5], [1, 2, 3])
print(list(a))
import itertools

b = itertools.starmap(abs, [(1,), (2,), (-3,), (4,), (-5,)])
print(list(b))
"""以下操作会报错，因为可迭代对象中存储的不是元组"""
#c = itertools.starmap(abs, [1, 2, 3, 4, 5])
#print(list(c))
"""注意starmap的用法"""
"""当函数的参数在可迭代对象中已经用元组形式组合起来时用itertools.starmap,否则用map"""
