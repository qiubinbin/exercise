file_path='text_files/Alice in Wonderland.txt'
with open(file_path,'r') as temp:
	content=temp.read()
	print(content.count('is'))
	print(content.lower().count('is'))