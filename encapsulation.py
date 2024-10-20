class wednesday:
    def __init__(self):
        self.a=10
        self._b=20
        self.__c=30
    def modifiers(self):
        print(obj1.a)
        print(obj1._b)
        print(obj1.__c)
    def setter(self):
        self.__c=int(input("Enter new value:"))
    def getter(self):
        return self.__c
        
obj1=wednesday()

#obj1.modifiers()
#print(obj1.a)#public access modifiers(access anywhere)
#print(obj1._b)#protected access modifiers(access only within same package)
#print(obj1.__c)#private access modifiers(access only within same class)
#obj1.setter()
print(obj1.getter())
