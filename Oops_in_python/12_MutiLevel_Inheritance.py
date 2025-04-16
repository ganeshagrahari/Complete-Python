class Car:
    @staticmethod
    def start():
        print("car stared..")
    
    @staticmethod
    def stop():
        print("Car stopped..")    
        
class ToyotaCar(Car):
    def __init__(self,name):
        self.name=name 
    
class Innova(ToyotaCar):
    def __init__(self, engine):
        self.engine = engine

car1=Innova("2.4D")   
car1.start()     
        
