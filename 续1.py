# favorite_languages = {
# 	'jen': ['python', 'ruby'],
# 	'sarah': ['c'],
# 	'edward': ['ruby', 'go'],
# 	'phil': ['python', 'haskell'],
# }
# for m in favorite_languages:
# 	if len(favorite_languages[m]) > 1:
# 		print(m.title()+ "'s favorite is")
# 		for n in favorite_languages[m]:
# 			print(n.lower())
# 	else:
# 		print(m.title())
# 		print('favorite language is: '+favorite_languages[m][0].lower())
# customer={
# 	'bob':{'first':'kaj','second':'huds','number':123},
# 	'bill':{'first':'jigu','second':'huhs','number':456},
# }
# for m,n in customer.items():
# 	print(m.title())
# 	print(n['first']+' '+n['second'])
# 	print('number is '+str(n['number']))
#
# prompt = "\nTell me something, and I will repeat it back to you:"
# prompt += "\nEnter 'quit' to end the program. "
# message = ""
# b=(message.lower() != 'quit') #error
# while b:
# 	message = input(prompt)
# 	print(message)
# 	b = (message.lower() != 'quit')

# while True:

# 	print(7)
# user=['tom','apple','jane']
# end=[]
# while user:
# 	done=user.pop()
# 	end.append(done)
# 	print("Verifying user: " + done.title())
# print("\nThe following users have been confirmed:")
# print(end)

# pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
# print(pets)
# while 'cat' in pets:
# 	pets.remove('cat')
# print(pets)

# answer={}
# a=input('输入名字：')
# b=input('输入号码: ')
# while a != 'quit' and b != 'quit':
# 	answer[a] = b
# 	a=input('输入名字：')
# 	b=input('输入号码: ')
# print(answer)

# JUDGE=True
# result={}
# while JUDGE:
# 	name=input('please input name: ')
# 	answer=input('please input answer: ')
# 	result[name]=answer
# 	judge=input('yes or no: ')
# 	if judge=='no':
# 		JUDGE=False
# apple=['a','b','c']
# for m in apple:
# 	print(m)
# def show(name):
# 	print('hello '+name.title()+'. ')
#
# show('qiubin')
# def describr(type,hum,name='zhuzhu'):
# 	print('\nType is '+type)
# 	print('Name is '+name)
# 	print('Else is '+hum)
#
#
# # describr('dog','has')
# # describr('cat','gg')
# # describr(name='pig',type='jk')
# describr(hum='hu',type='gg')
# def show_full_name(fisrt_name,last_name,middle_name=''):
# 	if middle_name:
# 		fullname = fisrt_name.title() + ' '+middle_name.title()+' ' + last_name.title()
# 	else:
# 		fullname=fisrt_name.title()+' '+last_name.title()
# 	return fullname
#
# musician=show_full_name('qiu','xiao','bin')
# print(musician)
# def fill_dictionary():
# 	JUDGE = True
# 	result = {}
# 	while JUDGE:
# 		name = input('please input name: ')
# 		answer = input('please input answer: ')
# 		result[name] = answer
# 		judge = input('yes or no: ')
# 		if judge == 'no':
# 			JUDGE = False
# 	return result
# print(fill_dictionary())
# def get_formatted_name(first_name, last_name, middle_name=''):
# 	"""返回整洁的姓名"""
# 	if middle_name:
# 		full_name = first_name + ' ' + middle_name + ' ' + last_name
# 	else:
# 		full_name = first_name + ' ' + last_name
# 	return full_name.title()
# musician = get_formatted_name('jimi', 'hendrix')
# print(musician)
# musician = get_formatted_name('john', 'hooker', 'lee')
# print(musician)
# def show_name(names):
# 	for name in names:
# 		print("Hello,"+name.title()+' !')
# example=['qiu','bin','ss']
# show_name(example)
# def show(name=''):
# 	if name:
# 		for x in name:
# 			print('Hello '+x.title())
# 	else:
# 		print("Please input: ")
#
# def get(result):
# 	while True:
# 		show()
# 		Name=input('Your name: ')
# 		result.append(Name)
# 		judge=input('Go on?')
# 		if judge=='no':
# 			break
# 	return result
#
# result=[]
# get(result)
# show(result)
# def show_name(names):
# 	while names:
# 		temp_name=names.pop()
# 		print("Hello,"+temp_name.title()+' !')
# example=['qiu','bin','ss']
# show_name(example)
# print(example)
# example1=['ll','mm']
# show_name(example1[:])
# print(example1)
# def show_toppings(*topppings):
# 	print('Made by those： ')
# 	print(topppings)
# 	for topping in topppings:
# 		print('- '+topping)
#
# show_toppings('apple')
# show_toppings('pepper','apple')
# import make_pizza
# from make_pizza import *
# print(make_pizza(3,2,one='pepper',two='apple',three='ss'))
# class Dog():
# 	def __init__(self,name,age): #根据Dog类创建新实例时，Python都会自动运行它
# 		self.name=name
# 		self.age=age
# 	def jump(self):
# 		print('Jump!')
#
# my_dog=Dog('gua',18)
# print(my_dog.name.title())
# my_dog.jump()

# my_new_car = Car('audi', 'a4', 2016)
# print(my_new_car.get_descriptive_name())
# my_new_car.read_odometer()
# my_new_car.odometer_reading=23
# my_new_car.read_odometer()
# my_new_car.update_odometer(56)
# my_new_car.read_odometer()
# my_new_car.increment_odometer(100)
# my_new_car.read_odometer()
from car import *

my_tesla=ElectricCar('tesla','model s',2016)
print(my_tesla.get_descriptive_name())
my_tesla.fill_gas_tank()
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()