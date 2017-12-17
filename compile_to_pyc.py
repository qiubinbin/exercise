'''编译生成.pyc文件'''
import py_compile
py_compile.compile('temp.py')
"""
当前路径包含temp.pyc的情况下，可以直接使用import temp
"""