def func(i):
    a=b=c=d=0
    if len (i)<6 or len (i)>12 :
        return 0
    for j in i:
        if j.isnumeric():
            a=1
        elif j.isupper():
            b=1
        elif j.islower():
            c=1
        elif j=='$' or j=='#' or j== '@':
            d=1
    if a and b and c and d:
        return 1

lst=input().split(",")
ls=[]
for i in lst:
    if func(i):
        ls.append(i)
print(",".join(ls))
