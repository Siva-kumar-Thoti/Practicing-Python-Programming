from math import sqrt

c,h=50,30

def calci(d):
    return sqrt((2*c*d)/h)

a=input().split(',')
a=[int(i) for i in a]
a=[str(int(calci(i))) for i in a]

print(",".join(a))
