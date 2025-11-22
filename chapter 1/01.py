'''
目录中关于chapter的章节, 主要是为了熟悉相关的包的简单函数，
主要内容参考《python机器学习入门与实战》
'''

'''
import numpy
numpy.array(object, dtype = None, copy = True, order = None, subok = False, ndim = ())
'''

import numpy as np

arr = np.array([10, 20, 30, 40, 50], dtype = complex, ndmin = 2)
print(arr)

lists1 = [[101, 202, 303], [404, 505, 606]]
arr1 = np.array(lists1)
print(arr1.dtype)
print(arr1.shape)

arr2 = np.zeros((3, 4))
print(arr2)

arr3 = np.ones((3, 4))
print(arr3)

arr4 = np.eye(4)
print(arr4)

arr5 = np.identity(3)
print(arr5)

arr6 = np.empty((3, 4))
print(arr6)

arr7 = np.array([12.5, 136.7, 24.6, 35.5, 109.8])
int_arr7 = arr7.astype(int)
print(int_arr7.dtype)
str_arr7 = arr7.astype(str)
print(str_arr7.dtype)

samples = np.random.normal(size = (4, 4))
print(samples)