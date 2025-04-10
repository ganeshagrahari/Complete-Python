#WAF to print n to 1
#by using loops first
'''def show(n):
    while(n>=1 ):
        print(n)
        n=n-1
show(5)  '''
#by using recursion
'''def show(n):
    if(n==0): #base case
        return
    print(n) #firstly we should write the work that it will do
    show(n-1) #fir se hi show call hua for (n-1)   
    print("END") 

show(3)      '''
 
#Waf recursive function to print factorial of a number 
def fact(n):
    if(n==0 or n==1):
        return 1
    return n*fact(n-1) #recursive call

print(fact(5)) 
        
        