# Lambda Function to Square a Number
square = lambda x: x ** 2
result = square(5)
print("Square Result:", result)

# Lambda Function for Addition
add = lambda x, y: x + y
result = add(3, 5)
print("Addition Result:", result)

# Lambda Function for Finding the Maximum
maximum = lambda x, y: x if x > y else y
result = maximum(10, 15)
print("Maximum Value:", result)

# Lambda Function for String Manipulation
uppercase = lambda s: s.upper()
result = uppercase("hello")
print("Uppercase Result:", result)

# Sorting a List of Tuples by the Second Element
points = [(1, 5), (3, 2), (2, 8)]
sorted_points = sorted(points, key=lambda x: x[1])
print("Sorted Points by Second Element:", sorted_points)

# Using Lambdas in Map and Filter
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x ** 2, numbers))
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Squared Numbers:", squared_numbers)
print("Even Numbers:", even_numbers)