class Mydivisble():
    def sevenMultiples(self,n):
        for i in range(0,n+1):
            if(i%7==0):
                yield i

instance=Mydivisble()
generator=instance.sevenMultiples(int(input()))

for i in generator:
    print(i)
