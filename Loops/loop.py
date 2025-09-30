##For Loops and the Range Function
for i in range(5):
    print(i)

##Using Range with Different Parameters
for i in range(1, 10, 2):
    print(i)

##Iterating in Reverse
for i in range(10, 0, -1):
    print(i)

##Looping Through Strings
str = "Krish Nayak"
for i in str:
    print(i)

##While Loops
count = 0
while count < 5:
    print(count)
    count += 1

##Break Statement
for i in range(10):
    if i == 5:
        break
    print(i)

##Continue Statement
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)

##Pass Statement
for i in range(5):
    if i == 3:
        pass
    print(i)

##Nested Loops
for i in range(3):
    for j in range(2):
        print(f"i = {i}, j = {j}")

##Sum of First n Natural Numbers
n = 10
sum = 0
count = 1
while count <= n:
    sum += count
    count += 1
print("Sum of first ten natural numbers is", sum)

##using for loop also-
sum = 0
for i in range(1, 11):
    sum += i
print("Sum of first ten natural numbers is", sum)

## Display Prime Numbers Between 1 and 100
for num in range(1, 101):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num)