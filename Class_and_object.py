
class employee:
    #special Method __init__ to initialize the attributes.
    #this is executed whenever an object is instantiated / constructed
    def __init__(self,name,age,height,salary):
        self.name = name     #every object needs to have value,
        self.age = age       #hence the assignments.
        self.height = height #Note: 'self' is the object.
        self.salary = salary

    def CalcSalry(self): #definition of Method
        sal = self.salary << 1 #1 shift = double, 2 shift = quadruple
        print(self.name, self.age, self.height, sal)

emp1 = employee("Biswajit", 30, 2, 500) #object instantiation

emp2 = employee("Soma", 20, 1.4, 1000) #object instatiation

emp1.CalcSalry() #calling Method from object emp1
emp2.CalcSalry() #calling Method from object emp2
