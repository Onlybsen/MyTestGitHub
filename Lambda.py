import Recursion as aa

#Use lambda or anonymous function
def lamb():
    val = (2,4,5,3,6,8,9,4)

    evens = list(filter(lambda n : n%2==0, val)) #anonymous function
    print(evens)
    print(id(evens))    #memory address
    print(type(evens))  #data type
    print(__name__)

if __name__ == "__main__":
    print('printed from', __name__)
    lamb()


