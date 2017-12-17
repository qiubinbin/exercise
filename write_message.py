filename = 'text_files\programming5.txt'
try:
	with open(filename, 'r') as file_object:
		print(file_object.read())
except FileNotFoundError:
	print('No file')
