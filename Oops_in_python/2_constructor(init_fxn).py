class Student:
    #Default-Constructor
    def __init__(self): #self ->reference of current object of the class>
       pass
   
    #Parameterized Constructor   
    def __init__(self,name,marks): #self ->reference of current object of the class>
        self.name = name
        self.marks=marks
        print("Adding new student in DataBase...")
        
s1 = Student("Ganesh Agrahari",97)  
print(s1.name,s1.marks) 

s2 = Student("Vishul Agrahari",100)    
print(s2.name,s2.marks)

        