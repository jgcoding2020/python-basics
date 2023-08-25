# Creating a dictionary
person = {"name": "Alice", "age": 30, "city": "New York"}

# Accessing elements by key
name = person["name"]
age = person["age"]

print("Accessing Elements:")
print("Name:", name)
print("Age:", age)

# Modifying dictionaries
person["age"] = 31  # Update the age
person["country"] = "USA"  # Add a new key-value pair
del person["city"]  # Delete a key-value pair

print("\nModifying Dictionaries:")
print("Modified Dictionary:", person)

# Dictionary keys, values, and items
keys = person.keys()
values = person.values()
items = person.items()

print("\nDictionary Keys, Values, and Items:")
print("Keys:", keys)
print("Values:", values)
print("Items:", items)

# Checking membership in keys
is_name_key_exists = "name" in person
is_email_key_exists = "email" in person

print("\nChecking Membership in Keys:")
print("Is 'name' a key?", is_name_key_exists)
print("Is 'email' a key?", is_email_key_exists)

# Dictionary iteration
print("\nDictionary Iteration:")
for key, value in person.items():
    print(f"{key}: {value}")

# Copying a dictionary
person_copy = person.copy()
print("\nCopying a Dictionary:")
print("Copy of Dictionary:", person_copy)

# Clearing a dictionary
person.clear()
print("\nClearing a Dictionary:")
print("Cleared Dictionary:", person)
