class identity:
    name = "siva"

    def __init__(self,name = None ):
        self.name = name

person1=identity("sheetal")
print("%s name is %s"%(identity.name,person1.name))

person2=identity()
person2.name="karnan"
print("%s name is %s"%(identity.name,person2.name))
