##simple addition function
def addition(a, b):
    return a + b
print(addition(2, 3))
# Output: 5

##Converting a Function to a Lambda Function
addition = lambda a, b: a + b
type(addition)  # Output: <class 'function'>
addition(5, 6)  # Output: 11

##Example: Checking Even Numbers
def even(num):
    if num % 2 == 0:
        return True
    else:
        return False

even(24)  # Output: True
##to convert lambda function of above code
even1 = lambda num: num % 2 == 0
even1(12)  # Output: True

##Lambda Functions with Multiple Parameters
def addition(x, y, z):
    return x + y + z
addition(12, 13, 14)  # Output: 39
#to convert into lambda function
addition1 = lambda x, y, z: x + y + z
addition1(12, 13, 14)  # Output: 39


##Using Lambda Functions with Map
numbers = [1, 2, 3, 4, 5, 6]
def square(number):
    return number ** 2

##Applying Square Function to a List
squared_numbers = list(map(lambda x: x ** 2, numbers))