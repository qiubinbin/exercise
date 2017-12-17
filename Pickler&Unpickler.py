import pickle
f = open('text_files/cat1.txt', 'wb')
a = pickle.Pickler(f)
a.dump('qiubin')
temp=7
a.dump(temp)
temp=8
a.dump(temp)
f.close()
f = open('text_files/cat1.txt', 'rb')
b = pickle.Unpickler(f)
print(b.load())
print(b.load())
print(b.load())