from array import *

arr = array('i',[])
n = int(input("Enter no. of array elements: "))
for i in range(n):
    val = int(input("Enter No.:"))
    arr.append(val)

print(arr)
idx = 0
v = int(input("Enter the value you want to search: "))
for k in arr:
    if k == v:
        print("Index=",idx)
        break
    idx += 1
else:
    print("not found")

#print(arr.index(v)) #will show error if v is not found in the arrayV
import numpy as np
arr1 = np.array([22,34],[23,43])
print(arr1)
