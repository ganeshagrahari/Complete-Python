class Account:
    def __init__(self,acc_no,acc_pass):
        self.acc_no=acc_no
        self.__acc_pass=acc_pass #making account pass private it can be called  outside the class
    
    def reset_pass(self): #this will not give an error because we are calling private attribute in side the class
        print(self.__acc_pass)    
    
acc1=Account("1234","8558")    

print(acc1.acc_no)
#print(acc1.__acc_pass)   # it will give an error
acc1.reset_pass() 

class Person:
    __name="Ganesh"
    
    def __hello(self):
        print("Hello User!")
        
    def welcome(self):
        self.__hello()
           

p1= Person()
#print(p1.__name)->error
#print(p1.__hello())->error
p1.welcome()