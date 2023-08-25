# Standard Input
name = input("Enter your name: ")
print("Hello, " + name)

# Reading from a File
with open("sample.txt", "r") as file:
    content = file.read()
    print("File Content:")
    print(content)

# Writing to a File
with open("output.txt", "w") as file:
    file.write("This is a line written to a file.\n")
    file.write("Another line written to a file.\n")

# Appending to a File
with open("output.txt", "a") as file:
    file.write("This line is appended to the file.\n")

# Reading and Writing Binary Files
with open("binary.bin", "wb") as file:
    binary_data = bytes([65, 66, 67, 68, 69])
    file.write(binary_data)

with open("binary.bin", "rb") as file:
    binary_content = file.read()
    print("Binary Content:", binary_content)

# Reading and Writing CSV Files (using the csv module)
import csv

data = [["Name", "Age"], ["Alice", 25], ["Bob", 30], ["Charlie", 35]]

# Writing to a CSV File
with open("data.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(data)

# Reading from a CSV File
with open("data.csv", "r") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print("CSV Row:", row)

# Reading and Writing JSON Files
import json

json_data = {"name": "Alice", "age": 25, "city": "New York"}

# Writing to a JSON File
with open("data.json", "w") as jsonfile:
    json.dump(json_data, jsonfile)

# Reading from a JSON File
with open("data.json", "r") as jsonfile:
    loaded_data = json.load(jsonfile)
    print("JSON Data:", loaded_data)
