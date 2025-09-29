##Arithmetic Operators
a = 10
b = 5
add_result = a + b
sub_result = a - b
mul_result = a * b
div_result = a / b
floor_div_result = a // b
modulus_result = a % b
exponential_result = a ** b

print(add_result)
print(sub_result)
print(mul_result)
print(div_result)
print(floor_div_result)
print(modulus_result)
print(exponential_result)

##Comparison Operators
a = 10
b = 10
result = a == b
print(result)

str1 = "Chris"
str2 = "Chris"
print(str1 == str2)
str3 = "chris"
print(str1 == str3)

print(str1 != str2)
print(str3 != str1)

## Greater Than and Less Than Operators

num1 = 45
num2 = 55
print(num1 > num2)
print(num1 < num2)
## Greater Than or Equal To and Less Than or Equal To

num1 = 45
num2 = 45
print(num1 >= num2)
print(num1 <= num2)
num1 = 44
print(num1 <= num2)

##Logical Operators
x = True
y = True
result = x and y
print(result)
y = False
result = x and y
print(result)

x = True
y = False
print(x or y)
x = False
y = False
print(x or y)

x = True
print(not x)
x = False
print(not x)

##Simple Calculator Example
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
print("Addition:", num1 + num2)
print("Subtraction:", num1 - num2)
print("Multiplication:", num1 * num2)
print("Division:", num1 / num2)
print("Modulus:", num1 % num2)
print("Exponential:", num1 ** num2)
