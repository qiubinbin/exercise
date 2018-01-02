import re

# a = 'qiuuqiubin2377qiu7邱彬\u4321'


# temp = r'qiu*'
# r = re.compile(temp)
# print(r.findall(a))
# print(re.findall(r,a))
# print(re.findall('.',a))
# print(re.match(r'1',a))
# print(re.search(r'iu??',a))
# print(re.findall(r'(?P<name>qiu)',a))
# print(re.split(r'i7',a))
# def pp(m):
#     if m.group()=='-':
#         return '?'
# print(re.sub(r'l*','6','qiu--bin',count=0))
# a1=re.compile(r'qiu')
# a2=re.match(r'qiu','qiubin')
# a2.groups()
# a2.end()


# temp = re.match(r'qiu',a)
# print(type(temp))
# print(re.escape(aa))
str1 = 'Guide will be out of the office from 12/15/2012 - 1/2/2012'
a = re.match(r'(?P<name>\d)hh\1', '7hh7')
b = re.match(r'7hh7', '7hh7gg')
c = re.compile(r'(\d+)/(\d+)/(\d+)')
f = c.finditer(str1)
d = re.compile(r'\d+/\d+/\d+')
e = d.findall(str1)
print(a.group())
print(b.group())
print(e)
for m in f:
    print(m.group())
print(re.sub(r'(\d+)/(\d+)/(\d+)', r'\2/\1/\3', str1))
print(re.findall(r'Hello(?!World)', 'HelloWorl1d'))
print(re.findall(r'(?<=Hello)World', 'HelloWorld'))
print(re.findall(r'(qiu)qiu\1', 'qiuqiuqiubin'))  # 注意此处的结果
print(re.findall(r'qiuqiu', 'qiuqiuqiubin'))
t=re.search(r'(qiu)77(\1)', 'qiu77qiubin')
print(t.group())
