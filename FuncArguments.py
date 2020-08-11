def sum(*a):  #variable length argument
    print(a)
    x = 0
    for i in a:
        print(i)
        x = x + i
    print(x)

sum(20,12,30,40,22)

def persdata(**kwdata): #keyworded variable length argument
    print(kwdata.items())
    for i,j in kwdata.items():
        print(i,j)

persdata(Name='Biswajit',dob='18/01/46', place='Singapore',Phone=84984343)


def names():
    i = 5
    lt =  0
    ge = 0
    while i > 0:
        name = input('Enter Name = ')
        if len(name) < 5:
            lt += 1
        else:
            ge += 1
        i -= 1
    return lt, ge

lt, ge = names()
print("Count of names LT 5 letters:",lt,"and GE 5 letters:",ge)
print("Count of names lt 5 letters: {} and ge 5 letters: {}".format(lt, ge))