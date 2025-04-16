'''class Circle:
    def __init__(self,r):
        self.r=r
        
    def area(self):
        return 3.14*self.r**2
    
    def perimeter(self):
        return 2*3.14*self.r

c1 = Circle(5)    
print(c1.area())
print(c1.perimeter())'''

'''class Employee:
    def __init__(self,role,department,salary):
        self.role=role
        self.deparment=department
        self.salary=salary
    
    def ShowDetails(self):
        print("role: ",self.role)
        print("department: ",self.deparment)
        print("salary: ",self.salary)

class Engineer(Employee):
    def __init__(self,name,age):
        self.name=name
        self.age=age  
        super().__init__("AI_engineer","AI","100k") 
    def ShowDetails(self):
        print(self.name)
        print(self.age)
        super().ShowDetails()
        
             

employee1 = Employee("AI Intern","Ai","100k")        
#employee1.ShowDetails()

e1= Engineer("Ganesh","20")
e1.ShowDetails()'''

class Order:
    def __init__(self,item,price):
        self.item=item
        self.price=price
        
    def __gt__(self,ord2):
        return self.price>ord2.price    


ord1=Order("car",100)
ord2=Order("helicoper",150)

print(ord1>ord2)
            
        
    