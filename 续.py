favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
	'mh':'c'
}
friends = ['phil', 'sarah']
for name in favorite_languages.keys():
	print(name.title())
	if name in friends:
		print(" Hi " + name.title() +
			", I see your favorite language is " +
			favorite_languages[name].title() + "!")
if 'qiubin' not in favorite_languages.keys():
	print("I'm boy!")
print(favorite_languages.values())
print(set(favorite_languages.values())) #set函数去除重复
a=[1,3,'r',(1,2)]
print(a)

pizza={'crust':'thick','toppings':['mushroom','cheese']}
print('You order a '+pizza['crust']+' pizza, made by following: \t')
for m in pizza['toppings']:
	print(m.title())
favorite_languages = {
	'jen': ['python', 'ruby'],
	'sarah': ['c'],
	'edward': ['ruby', 'go'],
	'phil': ['python', 'haskell'],
}
for m in favorite_languages:
	print("\n"+m+': ')
	for n in favorite_languages[m]:
		print(n.title())
for m,n in favorite_languages.items():
	print(m.title()+': ')
	for x in n:
		print(x.lower())
for m in favorite_languages:
	if len(favorite_languages[m]) > 1:
		print(m.title())
		for n in favorite_languages[m]:
			print(n.lower())
	else:
		print(m.title())
		print(favorite_languages[m][0].lower())