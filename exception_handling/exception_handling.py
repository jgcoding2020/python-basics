# Exception Handling - Handling Specific Exceptions
try:
    num = int(input("Enter a number: "))
    result = 10 / num  # Attempting division
    print("Result:", result)
except ZeroDivisionError:
    print("Error: Division by zero")
except ValueError:
    print("Error: Invalid input. Please enter a valid number")
except Exception as e:
    print("An error occurred:", str(e))
else:
    print("No exceptions occurred.")  # Executed if no exceptions are raised

# Exception Handling - Handling Multiple Exceptions in One Except Block
try:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    result = num1 / num2  # Attempting division
    print("Result:", result)
except (ZeroDivisionError, ValueError) as e:
    print("Error:", str(e))

# Exception Handling - Using Finally
try:
    file = open("nonexistent.txt", "r")  # Attempting to open a file
    content = file.read()
    print(content)
except FileNotFoundError:
    print("Error: File not found")
finally:
    if 'file' in locals():
        file.close()  # Closing the file if it was opened
        print("File closed (if it was open).")

# Raising Exceptions
try:
    age = int(input("Enter your age: "))
    if age < 0:
        raise ValueError("Age cannot be negative")  # Raising a custom exception
except ValueError as ve:
    print("Error:", str(ve))

# Custom Exception
class MyCustomException(Exception):
    def __init__(self, message):
        super().__init__(message)

try:
    raise MyCustomException("This is a custom exception")  # Raising and handling a custom exception
except MyCustomException as ce:
    print("Custom Exception:", str(ce))

# Finally Without Except
try:
    num = int(input("Enter a number: "))
    result = 10 / num  # Attempting division
    print("Result:", result)
finally:
    print("This will execute no matter what.")  # Executed regardless of exceptions

# Using 'with' Statement for File Handling
try:
    with open("file_does_not_exist.txt", "r") as file:  # Attempting to open a file
        content = file.read()
        print(content)
except FileNotFoundError as fnfe:
    print("File not found:", str(fnfe))
