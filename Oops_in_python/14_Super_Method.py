class Car:
    def __init__(self,type):
        self.type=type  
        
class ToyotaCar(Car):
    def __init__(self,name,type ):
        super().__init__(type)
        self.name=name 
        
    
car1=ToyotaCar("Innova Crysta","2.4D")               
print(car1.type)
