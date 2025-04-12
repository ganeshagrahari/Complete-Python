class Student:
    college_name= "BBD" # Class attribute
    name = "Anonymous"# Class attribute
    def __init__(self,name,branch):
        self.name=name
        self.brach=branch

s1 = Student("Ganesh","Ds and Ai")        
s2 = Student("Avishank","Ds and Ai")  
print(s1.name,s1.brach,s1.college_name) # obj attr>> class sttr
print(Student.college_name)