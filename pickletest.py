# from get&setstate import Foo
import pickle

foo = Foo(7, 'text_files/temp.txt')
with open('text_files/cat.txt','wb') as f:
	pickle.dump(foo,f)
