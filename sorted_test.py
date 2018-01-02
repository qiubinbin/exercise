def wraper(n):
    def sorter(m):
        return m[n]

    return sorter


"""按元组第一个数字排序"""
print(sorted([(1, 2), (7, 2), (4, 5)], key=wraper(0)))
"""按元组第二个数字排序"""
print(sorted([(1, 2), (7, 2), (4, 5)], key=wraper(1)))