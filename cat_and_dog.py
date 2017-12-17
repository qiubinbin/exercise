file_path=['text_files/dog.txt','text_files/dog.txt']
for path in file_path:
	try:
		with open(path,'r') as animal:
			names = animal.readlines()
	except FileNotFoundError:
		pass
		# print('找不到文件')
	else:
		temp=0
		while temp<len(names):
			names[temp]=names[temp].strip()
			temp+=1
		print(names)