# List Comprehension to Create a List of Squares
squares = [x ** 2 for x in range(1, 6)]
print("Squares:", squares)

# List Comprehension with Conditional Filtering
even_numbers = [x for x in range(1, 11) if x % 2 == 0]
print("Even Numbers:", even_numbers)

# List Comprehension to Process Elements
names = ["Alice", "Bob", "Charlie"]
name_lengths = [len(name) for name in names]
print("Name Lengths:", name_lengths)

# Nested List Comprehension to Flatten a List of Lists
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [num for row in matrix for num in row]
print("Flattened Matrix:", flattened)

# List Comprehension with Conditional Expression
numbers = [1, 2, 3, 4, 5]
squared_evens = [x ** 2 if x % 2 == 0 else x for x in numbers]
print("Squared Evens:", squared_evens)

# List Comprehension with Zip
fruits = ["apple", "banana", "cherry"]
colors = ["red", "yellow", "red"]
fruit_color_pairs = [(fruit, color) for fruit, color in zip(fruits, colors)]
print("Fruit-Color Pairs:", fruit_color_pairs)
