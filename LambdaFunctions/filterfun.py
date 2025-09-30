##Introduction to Python's Filter Function
def is_even(num):
    if num % 2 == 0:
        return True
    return False
print(is_even(3))

##Defining a Function to Check Even NumbersS
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

##Filtering a List Using the filter FunctionS
even_numbers = list(filter(is_even, numbers))
print(even_numbers)

##Using Lambda Functions with Filter
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
filtered_numbers = list(filter(lambda x: x > 5, numbers))
print(filtered_numbers)

##Filtering with Multiple ConditionsS
filtered_numbers = list(filter(lambda x: x > 5 and x % 2 == 0, numbers))
print(filtered_numbers)

##Filtering DictionariesS
people = [
    {'name': 'Jack', 'age': 32},
    {'name': 'John', 'age': 25},
    {'name': 'Jill', 'age': 33}
]

def age_greater_than_25(person):
    return person['age'] > 25

filtered_people = list(filter(age_greater_than_25, people))
print(filtered_people)