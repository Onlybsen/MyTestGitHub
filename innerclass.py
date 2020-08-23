
class student:
    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno
        self.lap = self.laptop("Acer","Pentium III","4gb") #creating object inside the outer class 'student'

    def show(self):
        print(self.name,self.rollno)
        print(s1.lap.show())

    class laptop:       #creating a class inside the class 'student'. Also called as Inner class
        def __init__(self,brand,cpu,ram):
            self.brand = brand
            self.cpu = cpu
            self.ram = ram

        def show(self):
            print(self.brand,self.cpu,self.ram)

s1=student("Naveen",19)
s2=student("Arora",21)

print(s1.name,s1.rollno,s1.lap.brand,s1.lap.cpu,s1.lap.ram) #using object 'lap' created inside class 'student'

lap1=student.laptop("Dell","i7","16gb") #creating 1st object outside the class 'student'
lap2=student.laptop("HP","i5","8gb")    #creating 2nd object outside the class 'student'
print(s1.name,s1.rollno,lap1.brand,lap1.cpu,lap1.ram)       #using object 'lap1' created outside class 'student'
print(s2.name,s2.rollno,lap2.brand,lap2.cpu,lap2.ram)       #using object 'lap2' created outside class 'student'

print(lap1.show())
print(lap2.show())