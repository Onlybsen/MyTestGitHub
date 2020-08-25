
class student:
    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno
        #self.lap = self.laptop("Acer","Pentium III","4gb") #creating object inside the outer class 'student'

    def show1(self):
        print(self.name,self.rollno)
        print(s1.lap.show())

class laptop(student):       #creating a class inside the class 'student'. Also called as Inner class
    def __init__(self,brand,cpu,ram):
        self.brand = brand
        self.cpu = cpu
        self.ram = ram

    def show2(self):
        print(self.brand,self.cpu,self.ram)

l1 = laptop("AA","3","xx")
print(l1.show2())