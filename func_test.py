import functools
'chifan'
def pp(m,n):
    return m+n
a=functools.partial(pp,4)
print(a(3))