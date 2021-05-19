suma=0
while 1:
    x=input()
    if len(x)==0:
        break
    l,a=x.split()
    if(l=='D'):
        suma+=int(a)
    else :
        suma-=int(a)

print(suma)    
        
    
