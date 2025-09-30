##Creating Lists
list = []
print(type(list))

##creating the lists and adding some elements of different datatypes
names = ['crush', 'Jack', 'Jacob']
mixed_list = [1, 'hello', 3.14, True]
print(names)
print(mixed_list)

##Accessing List Items
fruits = ['apple', 'banana', 'cherry', 'kiwi', 'guava']
print(fruits[0])  # apple
print(fruits[2])  # cherry
print(fruits[-1]) # guava

##Slicing Lists
print(fruits[1:])      # ['banana', 'cherry', 'kiwi', 'guava']
print(fruits[1:3])    # ['banana', 'cherry']
print(fruits[-1:])    # ['guava']

##Modifying List Elements
fruits[1] = 'watermelon'
print(fruits)

fruits[1:] = 'watermelon'
print(fruits)

##List Methods
fruits = ['apple', 'banana', 'cherry', 'kiwi', 'guava']
fruits.append('orange')
print(fruits)

fruits.insert(1, 'watermelon')
print(fruits)

fruits.remove('banana')
print(fruits)

pop_fruit = fruits.pop()
print(pop_fruit)
print(fruits)

index = fruits.index('cherry')
print(index)

fruits.insert(2, 'banana')
count = fruits.count('banana')
print(count)

fruits.sort()
print(fruits)

fruits.reverse()
print(fruits)

fruits.clear()
print(fruits)

##Slicing Lists: Advanced Examples
numbers = [1,2,3,4,5,6,7,8,9,10]
print(numbers[2:5])        # [3, 4, 5]
print(numbers[5:])         # [6, 7, 8, 9, 10]
print(numbers[::2])        # [1, 3, 5, 7, 9]
print(numbers[::-1])       # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
print(numbers[::-2])       # [10, 8, 6, 4, 2]

##Iterating Over Lists
for number in numbers:
    print(number)

for index, number in enumerate(numbers):
    print(index, number)

##List Comprehension
squares = []
for x in range(10):
    squares.append(x**2)
print(squares)

squares = [x**2 for x in range(10)]
print(squares)

##List Comprehension Syntax
even_numbers = [num for num in range(10) if num % 2 == 0]
print(even_numbers)

##Nested List Comprehension
list1 = [1, 2, 3, 4]
list2 = ['a', 'b', 'c', 'd']
pairs = [(i, j) for i in list1 for j in list2]
print(pairs)

##List Comprehension with Functions
words = ['hello', 'world', 'Python', 'list', 'comprehension']
lengths = [len(word) for word in words]
print(lengths)