# Methos that don't have the self parameter(works at class level):-
class Studnet:
    @staticmethod #decorator
    def college():
        print("BBDU")
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

s1 = Studnet("ganesh",90)            
s1.college()