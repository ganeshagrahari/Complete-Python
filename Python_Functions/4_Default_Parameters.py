#Default Parameters
# A default parameter is a parameter that assumes a default value if a value is not provided in the function call for that parameter.
def cal_product(a=1,b=1):
    print(a*b)

cal_product() # 1*1 = 1    
#non default arg follows default arg
def cal_sum(a,b=2):
    print(a+b)
    