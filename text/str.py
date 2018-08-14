"""Note
1. import 直接模块名字，是从sys.path list中检索，可以修改path让后再import
2. 本地模块和系统模块重名，优先本地
3. append返回为None,修改原来list
4. import导入的模块直接执行
5. sys.path list中第一个问本文件所在目录
"""
import string
import str1
import sys

s = 'The quick brown fox jumped over the lazy dog.'

print('==========')

print(sys.path)

print(sys.path.append('../'))

print(sys.path)


import pmodule


print(dir(str1))

print(s)

print(string.capwords(s))
