n = int(input())
def Fact(x):
    if x <= 1 : return 1
    else : return x*Fact(x-1)
print(Fact(n))

