class Student:
    def __init__(self,phy,chem,maths):
        self.phy=phy
        self.chem=chem
        self.maths=maths
        #self.percentage= str((self.phy+self.chem+self.maths)/3) +" %"
    @property
    def percentage(self):
        return str((self.phy+self.chem+self.maths)/3) +" %"

stu1 = Student(98,97,95)        
print(stu1.percentage)
stu1.maths=75
print(stu1.percentage)



        
        
        
        