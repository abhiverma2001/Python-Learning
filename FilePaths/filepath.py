##Creating a New Directory
import os
new_directory = 'package'
os.mkdir(new_directory)
print(f"Directory {new_directory} is created.")

##Listing Files and Directories
items = os.listdir('.')
print(items)

##Joining Paths
directory_name = 'folder'
file_name = 'file.txt'
full_path = os.path.join(directory_name, file_name)
print(full_path)
#getcwd() give the full path including the current working directory
full_path = os.path.join(os.getcwd(), directory_name, file_name)
print(full_path)

##Checking Path Existence
example_path = 'example1.txt'
if os.path.exists(example_path):
    print(f"The path {example_path} exists.")
else:
    print(f"The path {example_path} does not exist.")

##Checking if Path is a File or Directory
path = 'example.txt'
if os.path.isfile(path):
    print(f"The path {path} is a file.")
elif os.path.isdir(path):
    print(f"The path {path} is a directory.")
else:
    print(f"The path {path} is neither a file nor a directory.")

##Getting the absolute paths
relative_path = 'example.txt'
absolute_path = os.path.abspath(relative_path)
print(absolute_path)