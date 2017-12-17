import temp
print(temp.a+1)
import sys
print(sys.modules)
del sys.modules['temp']
print(sys.modules)