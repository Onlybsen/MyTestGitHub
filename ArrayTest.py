from array import *

arr = array('i', [])
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

print("Hello World")

print(arr.index(v)) #will show error if v is not found in the array, otherwise will show the index of v