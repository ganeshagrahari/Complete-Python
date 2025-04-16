class Person:
    name = "Anoymous"

    '''def changeName(self,name):
        Person.name = name
        #self.__class__.name="Ganesh" '''
    @classmethod
    def changename(cls,name):
        cls.name= name    

p1 = Person()        
p1.changeName("ganesh A")
print(p1.name)
print(Person.name)