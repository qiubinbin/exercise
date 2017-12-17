# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 11:13:38 2017

@author: qiubi
"""
cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
else:
    print(car.title())
car=['qiu','bin']
if car==['qiu','bin']:
	print(car)
b=2
if b not in car:
	print("x")
elif 'gg' in car:
	print()
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
	if requested_topping == 'green peppers':
		print("Sorry, we are out of green peppers right now.")
	else:
		print("Adding " + requested_topping + ".")
print("\nFinished making your pizza!")
requested_toppings = []
if requested_toppings:
	for requested_topping in requested_toppings:
		print("Adding " + requested_topping + ".")
	print("\nFinished making your pizza!")
else:
	print("Are you sure you want a plain pizza?")

available_toppings = ['mushrooms', 'olives', 'green peppers',
					  'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
for requested_topping in requested_toppings:
	if requested_topping in available_toppings:
		print("Adding " + requested_topping + ".")
	else:
		print("Sorry, we don't have " + requested_topping + ".")

alien_0 = {'color': 'green', 'points': 5} #字典
print(alien_0['color'])
print(alien_0['points'])

alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)
del alien_0['color']
print(alien_0)
favorite_color={
	'jen':'c',
	'jane':'c++',
	'ben':'java',
}
print(favorite_color)
for x,y in favorite_color.items():
	print("\nKey: "+x)
	print("Value: "+y)
for m in favorite_color.keys():
	print("\n n: "+m)
	print(favorite_color[m])