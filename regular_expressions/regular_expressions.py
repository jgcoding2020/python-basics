import re

# Basic Regular Expression Matching
text = "Hello, World! This is a test."
pattern = r"World"
matches = re.findall(pattern, text)
print("Basic Matching:", matches)

# Character Classes
text = "The cat and the hat sat on the mat."
pattern = r"[ch]at"
matches = re.findall(pattern, text)
print("Character Classes:", matches)

# Quantifiers
text = "The meeting will be held on June 15, 2023."
pattern = r"\d{2,4}"
matches = re.findall(pattern, text)
print("Quantifiers:", matches)

# Word Boundaries
text = "He's reading a book on cooking."
pattern = r"\bbook\b"
matches = re.findall(pattern, text)
print("Word Boundaries:", matches)

# Groups
text = "John Smith: 555-1234, Alice Johnson: 555-5678"
pattern = r"(\w+ \w+): (\d{3}-\d{4})"
matches = re.findall(pattern, text)
print("Groups:", matches)

# Alternation
text = "I love cats, but I also like dogs."
pattern = r"cats|dogs"
matches = re.findall(pattern, text)
print("Alternation:", matches)

# Character Escapes
text = "The cost is $19.99, on sale for 50% off!"
pattern = r"\$\d+\.\d{2}|[0-9]+%"
matches = re.findall(pattern, text)
print("Character Escapes:", matches)

# Search and Replace
text = "I have an apple, I have a banana."
pattern = r"I have (an|a) (\w+)"
replacement = r"You have \2"
result = re.sub(pattern, replacement, text)
print("Search and Replace:", result)

# Case-Insensitive Matching
text = "Python is pythOn, not pytHon."
pattern = r"python"
matches = re.findall(pattern, text, re.IGNORECASE)
print("Case-Insensitive Matching:", matches)
