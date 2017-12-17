while True:
	a=input('\nFirst number:')
	b=input('Second number:')
	try:
		print(float(a)+float(b))
	except ValueError:
		print('请输入两个数字')