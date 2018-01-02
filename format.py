a = 'qiu{0:<^10.2f}bin{1}'
print(a)
print(a.format(55, 2))
print('qiu%.3fbin' % 77)
b = {'name1': 77.2, 'name2': 55}
print("binbin{name1:0.4f}haha{name2}".format(name1=55, name2=4))
import string

temp = string.Formatter()
print(temp.format('chi{0}fan{1}', 55, 77))
print(temp.vformat('chi{0}fan{1}', (55, 77), {}))
for sw in temp.parse('qiu{name1!r:0.3f}bin{name2!s:?^4d}'):
    print(sw)
print(temp.get_value(4, (3, 4, 5, 'g', 'l'), {}))
print(temp.convert_field('qiubin', 's'))
print(temp.get_field('name1', (), {'name1': 77, 'name2': 44, 'name3': 'll'}))
print(temp.check_unused_args('name1',(), {'name7': 77, 'name2': 44, 'name3': 'll'}))
print('''chifan''')

temp1=string.Template('qiu$name')
print(temp1.safe_substitute({'name':77}))
print(temp1.template)
class test(string.Template):
    delimiter = '@'
temp2=test('qiu@{name}')
print(temp2.substitute({'name':78}))
print(string.capwords(' qiu    bin   '))
import re
pp=re.findall('[a-z]+','qiubiN',flags=re.I)
print(pp)
c=''.maketrans('qiubin','bsnqiu')
print(c)
print('qiubiin'.translate(c))