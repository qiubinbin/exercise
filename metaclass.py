"""类实现过程"""
class_name='Foo'
class_parents=(object,)#注意必须是元组，同时注意一元元组的写法
class_body="""
def __init__(self,x):
	self.x=x
def blah(self):
	print('Hello World')
"""
class_dict={}
#在局部字典class_dict中执行类主体,
exec(class_body,globals(),class_dict)
print(class_dict)
#创建类对象
Foo=type(class_name,class_parents,class_dict)
a=Foo(7)
print(a.x)