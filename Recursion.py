
import sys

#print(sys.getrecursionlimit())

def fact(n):
    if n == 0:
        return 1
    return n * fact(n-1)

result = fact(5)
print(result)

#Use lambda or anonymous function
val = (2,4,5,3,6,8,9,4)

evens = list(filter(lambda n : n%2==0, val))
print(evens)
