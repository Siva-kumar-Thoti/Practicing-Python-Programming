lst=input().split()
lst2=sorted(set(lst))

for i in lst2:
    print(i+":"+str(lst.count(i)))
