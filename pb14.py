lst=input()
u=l=0
for i in lst:
    if i.isalpha() :
        if i.isupper() :
            u+=1
        else:
            l+=1
print("UPPER CASE "+str(u))
print("LOWER CASE "+str(l))
            
