import numpy as np
#arr1 = np.array([22,34],[23,43])
arr1 = np.linspace(0,10,5)
print('arr1 =', arr1)
arr2 = np.linspace(0,10,2)
print('arr2 =',arr2)
arr3 = np.arange(0,10)
print('arr3 =',arr3)
arr4 = np.zeros(5,int)
print('arr4 = ',arr4)
arr5 = np.ones(5,int)
print('arr5 = ',arr5)
arr6 = np.array([[1,2,3,4],[4,3,2,1],[12,23,43,11]])
print(arr6)
print(arr6[2:])
print(arr6[2,3])
print(arr6.dtype)
print(arr6.size)
print(arr6.ndim)
print(arr6.shape)
a = ([3,4,3,33],[21,12,34,76])
arr7 = np.array(a)
print(arr7)
print(arr7.flatten()) #conver two-dimensional array into one

arr8 = arr7.reshape(4,2) #convert into two-dimensional array
print(arr8)

arr9 = np.array([[[4,3,5],[6,5,2]],[[7,4,9],[5,4,8]]]) #multi-dimensional
print(arr9)
print('********')

arrA = np.array([[1,2,4],[4,1,2],[3,4,1]])
arrB = np.array([[1,2,3],[4,5,4],[3,6,2]])
print(arrA)
print(arrB)
arrC = arrA * arrB
print(arrC)

