##Defining a Square Function
def square(x):
    return x * x

##Using map to Apply the Function
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
squared_numbers = map(square, numbers)
result = list(squared_numbers)
print(result)

##Using Lambda Functions with map
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
squared_numbers = list(map(lambda x: x * x, numbers))
print(squared_numbers)

##Mapping Multiple Iterables
numbers_one = [1, 2, 3]
numbers_two = [4, 5, 6]
added_numbers = list(map(lambda x, y: x + y, numbers_one, numbers_two))
print(added_numbers)

##Using map for Type Conversion
string_numbers = ['1', '2', '3', '4']
int_numbers = list(map(int, string_numbers))
print(int_numbers)

##Applying String Methods with map
words = ['apple', 'banana', 'cherry']
upper_words = list(map(str.upper, words))
print(upper_words)

##Using map with a List of Dictionaries
def get_name(person):
    return person['name']

people = [
    {'name': 'Krish', 'age': 32},
    {'name': 'Jack', 'age': 33}
]
names = list(map(get_name, people))
print(names)