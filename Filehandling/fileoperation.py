##Reading a Whole File
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)

##Read a File line by line
with open('example.txt', 'r') as file:
    for line in file:
        print(line.strip())##strip() removes the newline character

##Writing a file(overwriting)
with open('example.txt', 'w') as file:
    file.write('Hello world.\n')
    file.write('This is a new line.\n')

##Appending to a File
with open('example.txt', 'a') as file:
    file.write('Append operation taking place.\n')

with open('example.txt', 'a') as file:
    file.write('Another appended line.\n')

##Writing a list of multiple lines to a files
lines = ['This is my first line.\n', 'Second line.\n', 'Third line.\n']
with open('example.txt', 'a') as file:
    file.writelines(lines)

##Working with binary files
with open('example.bin', 'wb') as file:
    file.write(b'Hello world. Some information.')

##for read a binary file in rb mode
with open('example.bin', 'rb') as file:
    content = file.read()
    print(content)

##Copying Content from One File to Another
##Read the content from a source text file and write to a destination file
with open('example.txt', 'r') as source_file:
    content = source_file.read()
with open('destination.txt', 'w') as destination_file:
    destination_file.write(content)

##Counting Lines, Words, and Characters in a File
def count_file_stats(filepath):
    with open(filepath, 'r') as file:
        lines = file.readlines()
        num_lines = len(lines)
        num_words = sum(len(line.split()) for line in lines)
        num_chars = sum(len(line) for line in lines)
    return num_lines, num_words, num_chars

lines, words, chars = count_file_stats('example.txt')
print(f'Lines: {lines}, Words: {words}, Characters: {chars}')

##Writing and then reading a file
with open('example.txt', 'w+') as file:
    file.write('Hello world.\n')
    file.write('This is a new line.\n')
    ##Move the file cursor to beginning
    file.seek(0)
    ##Read the content of the file
    content = file.read()
    print(content)