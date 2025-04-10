#q1---> waf to find the sum of n natural numbers
'''def sum_n(n):
    if(n==0):
        return 0
    return sum_n(n-1)+n

print(sum_n(5))'''
#q2-->write a recursive function to print all element of a list
def print_ele(list,idx=0):
    if(idx==len(list)):
        return
    print(list[idx])    
    print_ele(list,idx+1)

a =[1,2,5,5,"ganesh"]
print_ele(a)

   