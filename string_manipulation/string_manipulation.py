# Concatenation
str1 = "Hello,"
str2 = " World!"
result = str1 + str2
print("Concatenation:", result)

# String Formatting
name = "Alice"
age = 30
formatted_str = f"My name is {name} and I am {age} years old."
print("String Formatting:", formatted_str)

# String Length
text = "Python is fun!"
length = len(text)
print("String Length:", length)

# String Indexing and Slicing
message = "Hello, Python!"
first_char = message[0]
substring = message[7:13]
print("First Character:", first_char)
print("Substring:", substring)

# Uppercase and Lowercase
text = "Python is Great!"
uppercase_text = text.upper()
lowercase_text = text.lower()
print("Uppercase:", uppercase_text)
print("Lowercase:", lowercase_text)

# String Splitting
csv_data = "Alice,Bob,Charlie,David"
names = csv_data.split(",")
print("String Splitting:", names)

# Joining Strings
words = ["Hello", "World", "!"]
sentence = " ".join(words)
print("Joining Strings:", sentence)

# Removing Whitespace
text_with_whitespace = "   This has leading and trailing spaces.   "
trimmed_text = text_with_whitespace.strip()
print("Whitespace Removal:", trimmed_text)

# Replacing Substrings
original_text = "I like ice cream."
modified_text = original_text.replace("ice cream", "chocolate")
print("String Replacement:", modified_text)

# Checking Substrings
text = "Python is awesome!"
contains_python = "Python" in text
contains_java = "Java" in text
print("Contains 'Python':", contains_python)
print("Contains 'Java':", contains_java)

# String Formatting with % (Legacy)
name = "Alice"
age = 30
formatted_str = "My name is %s and I am %d years old." % (name, age)
print("String Formatting (Legacy):", formatted_str)