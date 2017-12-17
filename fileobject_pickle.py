if __name__ == '__main__':
	print('test')
else:
	class Foo():
		def __init__(self, value, filename):
			self.value = value
			self.logfile = open(filename, 'w')

		def __getstate__(self):
			'''返回需要被序列化的列表'''
			f = self.logfile
			return (self.value, f.name, f.tell())  # tell()返回当前指针位置

		def __setstate__(self, state):
			"""从反序列化的state中读取数据"""
			self.value, name, position = state
			f = open(name, 'w')
			f.seek(position)
			self.logfile = f
			self.__class__ = NewFoo


	class NewFoo():
		test = 8

		def __init__(self, value, filename):
			self.value = value
			self.logfile = open(filename, 'w')

		def __getstate__(self):
			"""Return state values to be pickled."""
			f = self.logfile
			return (self.value, f.name, f.tell())  # tell()返回当前指针位置

		def __setstate__(self, state):
			"""Restore state from the unpickled state values."""
			self.value, name, position = state
			f = open(name, 'w')
			f.seek(position)
			self.logfile = f
