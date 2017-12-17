"""利用@contextlib.contextmanager和yield生成器实现上下文管理"""
import contextlib


@contextlib.contextmanager
def pp(m):
	print('begin')
	m += 1
	yield m  # 把传递给yield的值用作__enter__()方法的返回值
	"""只有在with语句块执行未出现错误时才会执行下面的语句(可以使用finally代替)"""
	print('end')


with pp(6) as temp:
	try:
		print(temp / 0)
	except ZeroDivisionError:
		pass
