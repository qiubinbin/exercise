def countN1(m):
    temp = []
    def pp(i):
        def pp1():
            return i * i
        return pp1

    for i in range(1, m + 1):
        temp.append(pp(i))
    return temp


a, b, c = countN1(3)
print(a(), b(), c())
"""当把函数当成对象返回时，注意不要包含可变对象，比如下面的操作"""
def countN2(m):
    temp = []

    for i in range(1, m + 1):
        def pp():
            return i * i
        temp.append(pp)


    return temp


a, b, c = countN2(3)
print(a(), b(), c())
