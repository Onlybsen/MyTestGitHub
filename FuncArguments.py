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

persdata(Name='Biswajit',dob='08/10/60', place='Kolkata',Phone=84984343)