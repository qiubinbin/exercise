"""利用__enter__和__exit__函数以及with语句实现上下文管理"""


class Test():
	def __init__(self, m):
		self.test = m

	def __enter__(self):
		print('begin')
		return self.test

	def __exit__(self, exc_type, exc_val, exc_tb):
		if not exc_type:
			print('end')
		else:
			print('error')


with Test(7) as temp:
	print(temp / 0)
