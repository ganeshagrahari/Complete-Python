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
    
car1=ToyotaCar("Innova Crysta")               
car1.start()
