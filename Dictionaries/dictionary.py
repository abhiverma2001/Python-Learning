##Creating Dictionaries
empty_dict = {}
print(type(empty_dict))
empty_dict2 = dict()
print(type(empty_dict2))

student = {'name': 'Krish', 'age': 32, 'grade': 24}
print(student)
print(type(student))

student = {'name': 'Krish', 'age': 32, 'name': 24}
print(student)

##Accessing Dictionary Elements
student = {'name': 'Krish', 'age': 32, 'grade': 'A'}
print(student['grade'])
print(student['age'])

print(student.get('grade'))
print(student.get('last_name'))
print(student.get('last_name', 'Not Available'))

##Modifying Dictionary Elements
student['age'] = 33
student['address'] = 'India'
print(student)

del student['grade']
print(student)

##Common Dictionary Methods
keys = student.keys()
print(keys)
values = student.values()
print(values)
items = student.items()
print(items)

student_copy = student
print(student)
print(student_copy)
student['name'] = 'Krish2'
print(student)
print(student_copy)

student_copy1 = student.copy()
print(student)
print(student_copy1)
student['name'] = 'Krish3'
print(student)
print(student_copy1)

##Iterating Over Dictionaries
for key in student.keys():
    print(key)
for value in student.values():
    print(value)
for key, value in student.items():
    print(f"{key}: {value}")

##Nested Dictionaries
students = {
    'student1': {'name': 'Krish', 'age': 32},
    'student2': {'name': 'Peter', 'age': 35}
}
print(students)

print(students['student2']['name'])
print(students['student2']['age'])

for student_id, student_info in students.items():
    print(f"{student_id}: {student_info}")
    for key, value in student_info.items():
        print(f"{key}: {value}")

##Dictionary Comprehension
squares = {x: x**2 for x in range(5)}
print(squares)

evens = {x: x**2 for x in range(10) if x % 2 == 0}
print(evens)

##Practical Example: Counting Frequency of Elements in a List
numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
frequency = {}
for number in numbers:
    if number in frequency:
        frequency[number] += 1
    else:
        frequency[number] = 1
print(frequency)

##Practical Example: Merging Two Dictionaries
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
merged_dict = {**dict1, **dict2}
print(merged_dict)
