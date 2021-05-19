x=y=0

while 1:
    a=input().split()
    if len(a)==0:
        break
    dire,units=map(str,a)
    units=int(units)
    if(dire=="UP"):
        x+= units
    if(dire=="DOWN"):
        x-= units
    if(dire=="LEFT"):
        y-= units
    if(dire=="RIGHT"):
        y+= units


from math import sqrt

z=sqrt(x**2 + y**2)
z=int(z)

print(z)
