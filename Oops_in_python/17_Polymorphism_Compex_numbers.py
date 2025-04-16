class Complex:
    def __init__(self,real,ima):
        self.real=real
        self.ima=ima
    
    def showNumber(self):
        print(self.real,"i +",self.ima,"j")  
    
    def __add__(self,num2):
         newReal = self.real+num2.real
         newIma = self.ima+num2.ima
         
         return Complex(newReal,newIma)   
      
    def __sub__(self,num2):
         newReal = self.real-num2.real
         newIma = self.ima-num2.ima
         
         return Complex(newReal,newIma)    
    
        
num1= Complex(3,4)
num1.showNumber()
num2=Complex(7,8)

num3=num1-num2
num3.showNumber()
