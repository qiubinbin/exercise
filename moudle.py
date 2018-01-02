import RE_test
print(RE_test.a + 1)
import sys
print(sys.modules)
del sys.modules['temp']
print(sys.modules)