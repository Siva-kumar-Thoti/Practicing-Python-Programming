def func(x,y):
    a=len(x)
    b=len(y)
    if a>b :
        print(x)
    elif a<b :
        print(y)
    else :
        print(x)
        print(y)

a,b=input().split()

func(a,b)
