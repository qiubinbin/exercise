import itertools
#
a = [1, 2, 3, 4, 5]
b = {'qiubin': 1, 'qiubin1': 2}
c = itertools.chain(a, b)
"""链接迭代器a,b"""
for temp in c:
    print(temp)
for m in itertools.chain.from_iterable([a, b, 'ABC']):
    """链接迭代器"""
    print(m)
# for temp in itertools.combinations('qiubin', 2):
#     """"组合数"""
#     print(temp)
# print('---------------')
# for temp in itertools.permutations('qiubin', 2):
#     """"排列数"""
#     print(temp)
# for temp in itertools.count(10):
#     print(temp)
# d = itertools.groupby('qqbbi')
# for m in d:
#     print(m)
# e = itertools.filterfalse(lambda m: m > 0, [-1, 2, 3, -2])
# """仅生成表达式为假的项"""
# print(list(e))
# e1 = itertools.islice([1, 2, 3, 4, 5, 6], 0, 6, 2)
# """切片"""
# print(list(e1))
# e2 = itertools.zip_longest([1, 2, 3, 4], [4, 5, 6], 'qiubin', fillvalue='7')
# """生成元组迭代器"""
# print(list(e2))
# e3 = itertools.product([1, 2, 3], [7, 8, 9], repeat=1)
# """生成笛卡尔坐标len**repeat"""
# print(list(e3))
# e4 = itertools.repeat([1, 2, 3], times=3)
# print(list(e4))
#
#
# def p(m, n):
#     return m * n
#
#
# e5 = itertools.starmap(p, [(2, 5), (3, 2), (10, 3)])
# print(list(e5))
# e6 = itertools.takewhile(lambda m: m < 4, [1, 2, 3, 4, 5, 6])
# print(list(e6))
# e7 = itertools.dropwhile(lambda m: m < 3, [1, 2, 3, 4, 5, 6])
# print(list(e7))
# e8 = itertools.tee([1, 2, 3, 4, 5], 7)
# for temp in e8:
#     print(list(temp))
