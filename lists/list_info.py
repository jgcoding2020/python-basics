# Creating a list
fruits = ["apple", "banana", "cherry", "date"]

# Accessing elements
first_fruit = fruits[0]
second_fruit = fruits[1]

print("Accessing Elements:")
print("First Fruit:", first_fruit)
print("Second Fruit:", second_fruit)

# Modifying lists
fruits[1] = "grape"  # Change the second element
fruits.append("fig")  # Add an element to the end
fruits.insert(2, "kiwi")  # Insert an element at a specific index
fruits.remove("cherry")  # Remove a specific element
popped_fruit = fruits.pop()  # Remove and return the last element

print("\nModifying Lists:")
print("Modified List:", fruits)
print("Popped Fruit:", popped_fruit)

# Slicing lists
sliced_fruits = fruits[1:4]  # Get a slice of elements
print("\nSlicing Lists:")
print("Sliced Fruits:", sliced_fruits)

# List concatenation
more_fruits = ["mango", "orange"]
combined_fruits = fruits + more_fruits
print("\nList Concatenation:")
print("Combined Fruits:", combined_fruits)

# List repetition
repeated_fruits = fruits * 2
print("\nList Repetition:")
print("Repeated Fruits:", repeated_fruits)

# List length
num_fruits = len(fruits)
print("\nList Length:")
print("Number of Fruits:", num_fruits)

# Sorting lists
sorted_fruits = sorted(fruits)
print("\nSorting Lists:")
print("Sorted Fruits:", sorted_fruits)

# Reversing lists
reversed_fruits = list(reversed(fruits))
print("\nReversing Lists:")
print("Reversed Fruits:", reversed_fruits)

# Checking membership
is_apple_in_fruits = "apple" in fruits
is_pear_not_in_fruits = "pear" not in fruits
print("\nChecking Membership:")
print("Is 'apple' in fruits?", is_apple_in_fruits)
print("Is 'pear' not in fruits?", is_pear_not_in_fruits)
