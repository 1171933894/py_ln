import numpy as np
#创建矩阵
# array=np.array([[1,2,3],[1,2,3]])
# array = np.arange(1,10).reshape(3,3)
# array=np.random.randint(1,10,12).reshape(2,3,2)
# array=np.random.rand(9).reshape(3,3)
# array=np.random.randn(9).reshape(3,3)
# array=np.empty(9).reshape(3,3)
# array=np.ones(9).reshape(3,3)
# array=np.zeros(9).reshape(3,3)
# print(array)
# print(array.ndim)
# print(array.shape)
# print(array.size)
# print(array.dtype)

array=np.random.randint(1,10,9).reshape(3,3)
print(array)
# print(array)
# print(np.where(array>5,array,0))
# print(array)
# print(array[2][2])
# print(array[0])
# print(array[:,0])

#基本运算
# print(array.sum())
# print(array.sum(0))
# print(array.sum(1))

print(array+array)
print(array-array)
print(np.dot(array,array))
print(array.T)