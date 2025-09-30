##Syntax of a Function
def function_name(parameters):
    """Docstring describing the function."""
    # Function body
    return value

##check if a number is even or odd not using function
num = 24
if num % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")

##Defining and Calling a Function
def even_or_odd(num):
    """This function finds if a number is even or odd."""
    if num % 2 == 0:
        print("The number is even")
    else:
        print("The number is odd")

even_or_odd(24)

##Functions with Multiple Parameters
def add(a, b):
    """Returns the sum of a and b."""
    return a + b

result = add(2, 4)
print(result)

##Default Parameters
def greet(name="guest"):
    print(f"Hello, {name}. Welcome to the Paradise.")

greet("Krish")
greet()

##Positional Arguments with *args
def print_numbers(*args):
    for number in args:
        print(number)

print_numbers(1, 2, 3, 4, 5, 6, "crash")

##Keyword Arguments with **kwargs
def print_detail(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_detail(name="Krish", age=32, country="India")

##Combining Positional and Keyword Arguments
def print_all(*args, **kwargs):
    print("Positional arguments:")
    for val in args:
        print(val)
    print("Keyword arguments:")
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_all(1, 2, 3, 4, 5, name="Krish", age=32)

##The Return Statement
def multiply(a, b):
    return a * b

result = multiply(2, 3)
print(result)

def multi_return(a, b):
    return a, b, a * b

x, y, product = multi_return(2, 3)
print(x, y, product)