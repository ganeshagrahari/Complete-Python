class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
        
    def hello(self):
        print("Hello,",self.name)
        
    def getmarks(self):
        return self.marks   

s1 = Student("Ganesh",100)           
s1.hello()
print(s1.getmarks())