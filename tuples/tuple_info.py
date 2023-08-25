# Creating a tuple
fruits = ("apple", "banana", "cherry", "date")

# Accessing elements
first_fruit = fruits[0]
second_fruit = fruits[1]

print("Accessing Elements:")
print("First Fruit:", first_fruit)
print("Second Fruit:", second_fruit)

# Tuple unpacking
fruit1, fruit2, fruit3, fruit4 = fruits
print("\nTuple Unpacking:")
print("Fruit 1:", fruit1)
print("Fruit 2:", fruit2)
print("Fruit 3:", fruit3)
print("Fruit 4:", fruit4)

# Length of a tuple
num_fruits = len(fruits)
print("\nLength of a Tuple:")
print("Number of Fruits:", num_fruits)

# Slicing a tuple
sliced_fruits = fruits[1:4]
print("\nSlicing a Tuple:")
print("Sliced Fruits:", sliced_fruits)

# Checking membership
is_apple_in_fruits = "apple" in fruits
is_pear_not_in_fruits = "pear" not in fruits
print("\nChecking Membership:")
print("Is 'apple' in fruits?", is_apple_in_fruits)
print("Is 'pear' not in fruits?", is_pear_not_in_fruits)

# Combining tuples
more_fruits = ("mango", "orange")
combined_fruits = fruits + more_fruits
print("\nCombining Tuples:")
print("Combined Fruits:", combined_fruits)

# Repeating a tuple
repeated_fruits = fruits * 2
print("\nRepeating a Tuple:")
print("Repeated Fruits:", repeated_fruits)

# Converting a list to a tuple
fruits_list = list(fruits)
print("\nConverting a List to a Tuple:")
print("Fruits List:", fruits_list)

# Converting a tuple to a list
fruits_tuple = tuple(fruits_list)
print("\nConverting a Tuple to a List:")
print("Fruits Tuple:", fruits_tuple)
