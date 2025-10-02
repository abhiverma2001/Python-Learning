##Introduction to Python Standard Library

##Working with Arrays
import array
arr = array.array('i', [1, 2, 3, 4])
print(arr)

##Math Module
import math
print(math.sqrt(4))
print(math.pi)

##Random Module
import random
print(random.randint(1, 10))
choices = ['apple', 'banana', 'cherry']
print(random.choice(choices))

##File and Directory access
import os
print(os.getcwd())
##os.mkdir('test_dir')

##High-Level File Operations with shutil
import shutil
shutil.copyfile('source.txt', 'destination.txt')

##Data Serialization with JSON
import json
data = {'name': 'Krish', 'age': 25}

json_str = json.dumps(data)
print(json_str)
print(type(json_str))

parsed_data = json.loads(json_str)
print(parsed_data)
print(type(parsed_data))

##Working with CSV Files
import csv

with open('example.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Name', 'Age'])
    writer.writerow(['Krish', 32])

with open('example.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)


##Date and Time Operations
from datetime import datetime, timedelta
now = datetime.now()
print(now)

yesterday = now - timedelta(days=1)
print(yesterday)

##Time Module
import time
print(time.time())
time.sleep(2)
print(time.time())

##Regular Expressions with re Module
import re
pattern = r'\d+'
text = 'There are 123 apples.'
match = re.search(pattern, text)
if match:
    print(match.group())