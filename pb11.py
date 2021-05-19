def btd(x):
    x=int(x)
    k=m=1
    sum=0
 
    while x:
        l=x%10
        k=l*m
        m=m*2
        x=int(x/10)
        sum+=k
        
    return sum
        
        

lst=input().split(",")
kmp=[]
for i in lst:
    if btd(i)%5==0 :
        kmp.append(str(i))
        
print(",".join(kmp))        
