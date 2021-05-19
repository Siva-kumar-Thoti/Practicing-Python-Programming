lst=input().split(",")
ls=[]
for i in lst:
    if (int(i)%2 != 0) :
        ls.append(str( int(i)**2 ) )
    
print(",".join(ls))
