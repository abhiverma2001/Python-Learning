##Creating Tuples
empty_tuple = ()
print(empty_tuple)
print(type(empty_tuple))

empty_list = list()
empty_tuple = tuple()
print(type(empty_list))
print(type(empty_tuple))

mixed_tuple = (1, "hello", 3.14, True)
print(mixed_tuple)

##Accessing Tuple Elements
numbers = (1, 2, 3, 4, 5, 6)
print(numbers[0])  # First element
print(numbers[-1])  # Last element
print(numbers[0:4])  # Slicing
print(numbers[::-1])  # Reverse tuple

##Tuple Operations
numbers = (1, 2, 3, 4, 5, 6)
mixed_tuple = (1, "hello", 3.14, True)
concatenation_tuple = numbers + mixed_tuple
print(concatenation_tuple)
repeated_tuple = mixed_tuple * 3
print(repeated_tuple)
repeated_numbers = numbers * 3
print(repeated_numbers)

##Immutability of Tuples
my_list = [1, 2, 3, 4, 5]
my_list[0] = "Krish"
print(my_list)
numbers = (1, 2, 3, 4, 5, 6)
numbers[1] = "Krish"  # This will raise an error

##Tuple Methods
numbers = (1, 2, 3, 4, 5, 6)
print(numbers.count(1))  # Counts occurrences of 1
print(numbers.index(3))  # Returns index of first occurrence of 3

##Packing and Unpacking Tuples
packed_tuple = (1, "hello", 3.14)
print(packed_tuple)
a, b, c = packed_tuple
print(a)
print(b)
print(c)

##Unpacking with Star
numbers = (1, 2, 3, 4, 5, 6)
first, *middle, last = numbers
print(first)
print(middle)
print(last)

##Nested Tuples and Lists
nested_list = [
    [1, 2, 3, 4],
    [6, 7, 9],
    [1, 1, "hello", 3.14, "C"]
]
print(nested_list[0])
print(nested_list[2][2])
print(nested_list[0:3])

nested_tuple = (
    (1, 2, 3),
    ("A", "B", "C"),
    (True, False)
)
print(nested_tuple[0])
print(nested_tuple[1][2])

##Iterating Over Nested Tuples
nested_tuple = (
    (1, 2, 3),
    ("A", "B", "C"),
    (True, False)
)
for sub_tuple in nested_tuple:
    for item in sub_tuple:
        print(item, end=" ")