def count(m):
    while m > 0:
        yield m
        m -= 1
    print('end')
    """利用for循环对生成器进行迭代时，收不到返回值"""
    return 'Test'


a = count(7)
for temp in a:
    print(temp)
b = count(7)
while True:
    try:
        temp = next(b)
        print(temp)
    except StopIteration as e:
        """捕获count的返回值"""
        print(e.value)
        break
