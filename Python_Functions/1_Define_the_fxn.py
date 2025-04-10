# Define a function...
# A function is a block of code that only runs when it is called

#function definition
def calc_sum(a,b): #parameters are a and b
    # This function takes two numbers and returns their sum
    return a+b

# Call the function with arguments 3 and 5
#function call
sum=calc_sum(3,5) #parameters are a and b 
print("The sum is:",sum)


# The fucntion for printing hello
def print_hello():
    print("Hello World!")

# Call the function to print hello
print_hello()
output = print_hello()
print(output) # This will print None because the function does not return anything