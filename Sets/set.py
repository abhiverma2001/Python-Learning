##Creating Sets
my_set = {1, 2, 3, 4, 5}
print(my_set)
print(type(my_set))

empty_set = set()
print(empty_set)
print(type(empty_set))

my_set = set([1, 2, 3, 4, 5, 6])
print(my_set)

##Properties of Sets
my_set = {1, 2, 3, 4, 5, 6, 6, 5}
print(my_set)

##Basic Set Operations: Adding and Removing Elements
my_set.add(7)
print(my_set)

my_set.add(7)
print(my_set)

my_set.remove(3)
print(my_set)
# This will raise an error if element is not present
# my_set.remove(10)

my_set.discard(10)
print(my_set)

removed_element = my_set.pop()
print('Removed element:', removed_element)
print(my_set)

my_set.clear()
print(my_set)

##Membership Test
my_set = {1, 2, 3, 4, 5}
print(3 in my_set)  # True
print(10 in my_set) # False

##Mathematical Set Operations
set_one = {1, 2, 3, 4, 5, 6}
set_two = {4, 5, 6, 7, 8, 9}

##Union
union_set = set_one.union(set_two)
print(union_set)  # Output: {1, 2, 3, 4, 5, 6, 7, 8, 9}

##Intersection
intersection_set = set_one.intersection(set_two)
print(intersection_set)

##Intersection Update
set_one.intersection_update(set_two)
print(set_one)  # Output: {4, 5, 6}

##Difference
set_one = {1, 2, 3, 4, 5, 6}
set_two = {4, 5, 6, 7, 8, 9}
difference_set = set_one.difference(set_two)
print(difference_set)  # Output: {1, 2, 3}

##Difference Update
set_one.difference_update(set_two)
print(set_one)  # Output will be updated accordingly

##Symmetric Difference
set_one = {1, 2, 3, 4, 5, 6}
set_two = {4, 5, 6, 7, 8, 9}
symmetric_diff_set = set_one.symmetric_difference(set_two)
print(symmetric_diff_set)  # Output: {1, 2, 3, 7, 8, 9}

##Set Methods: Subset and Superset
set_one = {1, 2, 3}
set_two = {3, 4, 5}

print(set_one.issubset(set_two))  # False
print(set_one.issuperset(set_two))  # False

##Removing Duplicates from a List Using Sets
my_list = [1, 2, 2, 3, 4, 4, 5]
unique_elements = set(my_list)
print(unique_elements)  # Output: {1, 2, 3, 4, 5}

##Practical Example: Counting Unique Words in Text
text = "In this tutorial we are discussing about sets."
words = text.split()
unique_words = set(words)
print(unique_words)
print('Number of unique words:', len(unique_words))
