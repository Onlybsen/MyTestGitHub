
from time import sleep
from threading import *    #Need to import threading package to use multi-threading
class student(Thread):     #student is a sub-class of Thread
    def __init__(self, name, rollno):
        Thread.__init__(self)
        self.name = name
        self.rollno = rollno

    def run(self):          #run() method is a must. this is a method available inside the class Thread
        for i in range(3):
            print(self.name,self.rollno)
            sleep(0.5)

class laptop(Thread):       #laptop is a sub-class of Thread
    def __init__(self,brand,cpu,ram):
        Thread.__init__(self)
        self.brand = brand
        self.cpu = cpu
        self.ram = ram

    def run(self):          #run() method is a must. this is a method available inside the class Thread
        for i in range(3):
            print(self.brand,self.cpu,self.ram)
            sleep(0.5)

st=student("Naveen",19)
lap=laptop("Dell","i7","16gb")

st.start()
sleep(0.2)   #this is to avoid collusion between the two threads. Do lap while st is sleeping
lap.start()
st.join()    #this is to request Main Thread to wait for the st to join
lap.join()   #this is to request Main Thread to wait for the lap to join
print("Bye") #will be executed by the Main Thread after completing 0f st and lap