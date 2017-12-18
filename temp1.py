import itertools

a = [1, 2, 3, 4, 1, 2, 5, 6, 7, 4, 2, 1]
a.sort()
b='qiubin'
temp=list(b)
print(temp)
temp.sort()
for m, n in itertools.groupby(temp):
    print(m)