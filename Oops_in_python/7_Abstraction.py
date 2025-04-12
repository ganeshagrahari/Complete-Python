# Abstraction : hinding the implementation details of the class and showing esstials features to user
class Car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch=False
    def start(self):
        self.clutch = True    
        self.acc = True   
        print("car started..")
    
car1 = Car()     
car1.start()
#Here we are hiding the implementation details of the class and showing esstials features to user.
#like the ability to start the car and control its acceleration and braking.
     
         