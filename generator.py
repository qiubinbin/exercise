def fib(m):
    """斐波那契数列"""
    a = 1
    b = 1
    while m > 0:
        yield a
        # temp=a
        # a=b
        # b=a+temp
        a, b = b, a + b  # 相比用temp更简洁的方法
        m -= 1


for m in fib(7):
    print(m)

import os

for temp in os.listdir('.'):
    """当前目录下的所有文件"""
    print(temp)

from scipy.special import comb
"""计算组合数C(m,n)"""


def pascal_tirangle(m):
    """杨辉三角"""
    n = 0
    while n < m:
        yield [int(comb(n, i)) for i in range(n + 1)]
        n += 1
for temp in pascal_tirangle(7):
    print(temp)