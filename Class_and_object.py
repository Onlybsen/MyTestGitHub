
class employee:
    compname = "ABC Co Pte Ltd" #class/static variable and it uses class namespace

    #special Method __init__ to initialize the attributes.
    #this is executed whenever an object is instantiated / constructed
    def __init__(self,name,age,height,salary):
        #following variables are instance variables and they use instance namespace
        self.name = name     #Note: every object needs to have value, hence the assignments.
        self.age = age       #'self' is a pointer to the object being used
        self.height = height
        self.salary = salary
        self.place = "Kolkata"

    def CalcSalry(self): #definition of Method
        sal = self.salary << 1 #1 shift = double, 2 shift = quadruple
        print('Company Name:', employee.compname,self.name, self.age, self.height, self.place, sal, )

    def compare(self,oth_obj):
        if self.salary == oth_obj.salary:
            return True
        else:
            return False

emp1 = employee("Biswajit", 30, 2, 500) #object instantiation/constructor
emp2 = employee("Soma", 20, 1.4, 1000) #object instatiation/constructor

emp1.place = "Singapore"

emp1.CalcSalry() #calling Method from object emp1
emp2.CalcSalry() #calling Method from object emp2

emp2.place = "My place"
print(emp2.place)
print(emp1.place)

if emp1.compare(emp2):  #passing the object emp2 to compare value between two oject members
    print('Salary same....')
else:
    print('Salary not same.....')

