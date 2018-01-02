"""利用埃式（Eratosthenes）算法找出所有的质数"""


def natural():
    """生成2开始的自然数"""
    n = 2
    while True:
        yield n
        n += 1


N = natural()


def filterN(prime):
    """筛选器"""
    return lambda m: m % prime > 0


def printN(m):
    while True:
        global N
        temp_prime = next(N)
        if temp_prime > 1000: break
        print(temp_prime)
        N = filter(filterN(temp_prime), N)


printN(1000)
"""生成小于1000的质数"""
