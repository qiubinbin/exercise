print('Input two numbers for devision!')
while True:
	a=input('Please input first number:')
	if a=='q':
		break
	b=input('Please input second number:')
	if b=='q':
		break
	try:
		print(float(a)/float(b))
	except ZeroDivisionError:
		print("You can't divide by 0!")
	else:
		print("It's OK!")