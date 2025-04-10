# q-->1:-WAF to print the length of a list
#a = [1,2,3]
#print(len(a))
'''def print_len(list):
    print(len(lsit))

print_len([1,2,4,5,7,7,10])    
a = "Ganesh"
print_len(a)
b = [1]
print_len(b)'''
#q---->2 WAF to print the element of a list in a single line .(list is the parameter)
'''a= [1,2,3,4,5]
for i in a:
    print(i,end =" ")

def print_ele(list):
    for i in list:
        print(i,end=" ") 

cities = ["Lucknow", "Noida", "Kanpur", "Pryagraj"]      
print_ele(cities)  '''
#q3-----> WAF to fine the factorial of n. (n is a parameter):
'''def find_factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact*=i
    return fact

factorial= find_factorial(5)    
print(factorial)'''
#q4---> WAF to cover USD to INR
'''def covert_into_inr(usd):
    return usd*82
inrvalue = covert_into_inr(2000)
print(inrvalue) '''
#q5--->waf to find that given no is even or odd
def odd_even(n):
    if(n%2==0):
        print("EVEN")
    else:
        print("ODD")    
num = int(input("Enter a number: "))    
odd_even(num)    