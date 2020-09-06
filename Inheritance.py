
class student:
    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno
        print("From student class:", self.name,self.rollno)
        #self.lap = self.laptop("Acer","Pentium III","4gb") #creating object inside the outer class 'student'

    def show1(self):
        print("From show1:",self.name,self.rollno)
        #print(s1.lap.show())

class laptop(student):       #Inheritance
    def __init__(self,brand,cpu,ram):
        super().__init__(brand,cpu)
        self.brand = brand
        self.cpu = cpu
        self.ram = ram
        super().show1()

    def show1(self):            #Method overloading
        print("Method overloading of show1()")

    def show2(self):
        print("From show2:", self.brand,self.cpu,self.ram)

l1 = laptop("AA","3","xx")
l1.show2()
l1.show1()