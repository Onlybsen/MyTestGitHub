
class student:
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def __add__(self,oth):
        m1 = self.a + oth.a   #st1.subject1 + st2.subject1
        m2 = self.b + oth.b   #st1.subject2 + st2.subject2
        m3 = self.a + self.b  #st1.subject1 + st1.subject2
        m4 = oth.a + oth.b    #st2.subject1 + st2.subject2

        st3 = student(m1,m2)
        st4 = student(m3,m4)
        return st3 #, st4   #returns the object consisting of subject1 and subject2 totals of st1 and st2

st1 = student(10,20)
st2 = student(34,12)

st3 = st1 + st2
print(st3.a,st3.b)

a = 5
b = 6

print(int.__add__(a,b)) #operator overloading
print(int.__sub__(a,b))
print(int.__mul__(a,b))
print(int.__mod__(a,b))