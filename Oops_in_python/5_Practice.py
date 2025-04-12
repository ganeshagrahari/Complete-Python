#q1---> Create Student class that takes names and marks of 3 subjects as argument in constructor then create a method to print the average
'''class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
        
    def average(self):
        sum = 0
        for i in self.marks:
            sum+=i
        
        return print(f"hi, {self.name} your average is {sum/len(self.marks)}")    
        

s1 = Student("Ganesh",[100,70,90,70,80,50,80])
s1.name = "Vishul"
s1.average()    '''
#q--2 create account class with two attribute - balance and ac no. create methods for debit, credit & printing the balance
class Account:
    def __init__(self,balance,ac_no):
        self.balance = balance
        self.ac_no = ac_no
        
    def debit(self,debit_amount):
        total_amount = self.balance-debit_amount
        print(f"your a/c has been debited with {debit_amount}, and your current balance is {total_amount}")
        self.balance-=debit_amount 
    
    def credit(self,credit_amount):
        total_amount = self.balance+credit_amount
        print(f"your a/c has been credited with {credit_amount}, and your current balance is {total_amount}") 
        self.balance+=credit_amount
    
    def print_balance(self):
        print("your a/c balance is: ",self.balance)           
ac1= Account(100000,864) 
ac1.print_balance()
ac1.debit(1000)
ac1.credit(1000)
ac1.credit(2000)
ac1.print_balance()
