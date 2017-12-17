import pickle

a = 1
b = a + 5
f = open('text_files/cat1.txt', 'wb')
pickle.dump(a, f)
pickle.dump(b, f)
f.close()
del a
f = open('text_files/cat1.txt', 'rb')
print(pickle.load(f))
print(pickle.load(f))