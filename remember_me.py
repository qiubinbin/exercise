import json

file_path1 = 'text_files\math.txt'


def get_stored_username(file_path):
	try:
		with open(file_path, 'r') as temp:
			b = json.load(temp)
	except FileNotFoundError:
		return None
	else:
		return b


def get_new_username(file_path):
	name = input('Please input name: ')
	with open(file_path, 'w') as temp1:
		json.dump(name, temp1)
		print('We will remember yours ' + name)


def greet_user(file_path):
	temp = get_stored_username(file_path)
	if temp:
		print('Hello ' + temp)
	else:
		get_new_username(file_path)


greet_user(file_path1)
