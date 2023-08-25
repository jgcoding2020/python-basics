# Importing a Standard Library Module
import math

# Using a Function from the math Module
result = math.sqrt(25)
print("Square Root of 25:", result)

# Renaming a Module
import datetime as dt

# Using a Function from the datetime Module
current_time = dt.datetime.now()
print("Current Time:", current_time)

# Importing Specific Functions from a Module
from random import randint, choice

# Using Functions from the random Module
random_number = randint(1, 10)
random_element = choice(['apple', 'banana', 'cherry'])
print("Random Number:", random_number)
print("Random Element:", random_element)

# Importing Everything from a Module (not recommended)
from statistics import *

# Using Functions from the statistics Module
data = [1, 2, 3, 4, 5]
mean_value = mean(data)
median_value = median(data)
print("Mean:", mean_value)
print("Median:", median_value)

# Creating and Importing a Custom Module
# Save this as mymodule.py
# def greeting(name):
#     return f"Hello, {name}!"

# In another script, import and use the custom module
# import mymodule
# result = mymodule.greeting("Alice")
# print(result)
