lst=input()
x=y=0
for i in lst:
    if i.isnumeric():
        x+=1
    elif i.isalpha():
        y+=1
print("LETTERS "+ str(y))
print("DIGITS "+ str(x))
    
