## NameError Exception
a=b

##Handling Exceptions with try and except
try:
    a = b
except:
    print("The variable has not been assigned.")

##also handle catch specific exceptions and display the error message
try:
    a = b
except NameError as x:
    print(x)
##Handling ZeroDivisionError
result = 1 / 0
#to handle this exception
try:
    result = 1 / 0
except ZeroDivisionError as x:
    print(x)
    print("Please enter the denominator greater than zero.")

##The Exception Base Class
try:
    a = b
except Exception as x1:
    print(x1)

##Handling Multiple Exceptions
try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ValueError:
    print("Not a valid number.")
except ZeroDivisionError:
    print("Enter denominator greater than zero.")
except Exception as x:
    print(x)

#Using else Block with try and except
try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ValueError:
    print("Not a valid number.")
except ZeroDivisionError:
    print("You can't divide the number by zero.")
except Exception as x:
    print(x)
else:
    print(f"The result is {result}")

#Using finally Block
try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ValueError:
    print("Not a valid number.")
except ZeroDivisionError:
    print("You can't divide the number by zero.")
except Exception as x:
    print(x)
else:
    print(f"The result is {result}")
finally:
    print("Execution complete.")

#Practical Example: File Handling with Exception Handling
try:
    file = open("example1.txt", "r")
    content = file.read()
    print(content)
except FileNotFoundError:
    print("The file does not exist.")
finally:
    if 'file' in locals() and not file.closed:
        file.close()
        print("File closed.")

#If another error occurs while reading the file, you can handle it with the Exception class.
try:
    file = open("example1.txt", "r")
    a = b  # This will raise NameError
except FileNotFoundError:
    print("The file does not exist.")
except Exception as x:
    print(x)
finally:
    if 'file' in locals() and not file.closed:
        file.close()
        print("File closed.")