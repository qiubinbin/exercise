def count_words(filename):
	'''计算文档字数'''
	try:
		with open(filename,encoding='utf-8') as f_obj:
			contents = f_obj.read()
	except FileNotFoundError:
		# msg = "Sorry, the file " + filename + " does not exist."
		# print(msg)
		pass
	else:
		# 计算文件大致包含多少个单词
		words = contents.split()
		num_words = len(words)
		print("The file " + filename + " has about " + str(num_words) + " words.")