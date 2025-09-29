##Declaring and assigning the variables
age = 32
height = 6.1
name = "Krish"
is_student = True

##Printing Variables
print("Age:", age)
print("Height:", height)
print("Name:", name)

##Naming Conventions for Variables
first_name = "Krish"
last_name = "Nayak"

### Invalid variable names
# 1age = 30  # Invalid: starts with a number
# first-name = "Krish"  # Invalid: contains a dash
# @name = "Krish"  # Invalid: contains @ symbol

##Case Sensitivity
name = "Krish"
Name = name
print(name == Name)  # False, as they are different identifiers

##Understanding Variable Types
age = 25  # int
height = 6.1  # float
name = "Krish"  # str
is_student = True  # bool
print(type(age))  # <class 'int'>
print(type(name))  # <class 'str'>

##Type Checking and Conversion
age = 25
print(type(age))  # int
age_str = str(age)
print(age_str)
print(type(age_str))  # str
age = "25"
print(type(int(age)))  # int
name = "Krish"
# int(name)  # This will raise an error: invalid literal for int()
height = 5.11
print(type(height))  # float
print(int(height))  # 5
print(float(int(height)))  # 5.0

##Dynamic Typing in Python
var = 10
print(var, type(var))  # 10 <class 'int'>
var = "Hello"
print(var, type(var))  # Hello <class 'str'>
var = 3.14
print(var, type(var))  # 3.14 <class 'float'>

##Input Function and Type Casting
age = input("What is the age? ")
print(age)
print(type(age))  # str

age = int(input("What is the age? "))
print(type(age))  # int


##Simple Calculator Example
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
sum_ = num1 + num2
difference = num1 - num2
product = num1 * num2
quotient = num1 / num2
print("Sum:", sum_)
print("Difference:", difference)
print("Product:", product)
print("Quotient:", quotient)
