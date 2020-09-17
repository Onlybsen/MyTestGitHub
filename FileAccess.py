
ifl = open("/users/user/swinst.bat", 'r')
ofl = open("MyData.txt",'w')
for d1 in ifl:
    ofl.write(d1)

