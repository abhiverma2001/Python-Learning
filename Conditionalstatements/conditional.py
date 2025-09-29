##The if Statement
age = 20
if age >= 18:
    print("You are allowed to vote in the elections.")

##The else Statement
age = 16
if age >= 18:
    print("You are eligible for voting.")
else:
    print("You are a minor.")

##The elif Statement
age = 20
if age < 13:
    print("You are a child.")
elif age < 18:
    print("You are a teenager.")
else:
    print("You are an adult.")

##Nested Conditional Statements
number = int(input("Enter the number: "))
if number > 0:
    print("The number is positive.")
    if number % 2 == 0:
        print("The number is even.")
    else:
        print("The number is odd.")
else:
    print("The number is zero or negative.")

##Example: Leap Year Calculation
year = int(input("Enter the year: "))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"{year} is a leap year.")
        else:
            print(f"{year} is not a leap year.")
    else:
        print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")

##Simple Calculator
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Enter operation (+, -, *, /): ")
if operation == '+':
    result = num1 + num2
    print(result)
elif operation == '-':
    result = num1 - num2
    print(result)
elif operation == '*':
    result = num1 * num2
    print(result)
elif operation == '/':
    if num2 != 0:
        result = num1 / num2
        print(result)
    else:
        print("Division by zero is not allowed.")
else:
    print("Invalid operation.")

##Ticket Price Based on Age
age = int(input("Enter your age: "))
is_student = input("Are you a student? (yes/no): ")
if age < 5:
    price = 0
elif age < 12:
    price = 10
elif age < 17:
    if is_student.lower() == 'yes':
        price = 12
    else:
        price = 15
else:
    price = 20
print(f"Ticket price: {price}")
