def func(x):
    flag=0 
    while x:
        l=x%10
        if(l%2!=0):
            flag=1
            break
        x=int(x/10)
        
    return 1 if flag==0 else 0

lst=[]
for i in range(1000,3001):
    if func(i)==1 :
        lst.append(str(i))
print(",".join(lst))        
        
