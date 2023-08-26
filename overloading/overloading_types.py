# Method Overloading with Default Arguments

class Calculator:
    def add(self, a, b=0):
        return a + b


# Create an instance of the Calculator class
calc = Calculator()

# Call the add method with different numbers of arguments
result1 = calc.add(5)
result2 = calc.add(3, 7)

print("Result 1:", result1)
print("Result 2:", result2)

# Method Overloading with Variable-Length Argument Lists


class Calculator:
    def add(self, *args):
        result = 0
        for num in args:
            result += num
        return result


# Create an instance of the Calculator class
calc = Calculator()

# Call the add method with different numbers of arguments
result1 = calc.add(5)
result2 = calc.add(3, 7)
result3 = calc.add(1, 2, 3, 4, 5)

print("Result 1:", result1)
print("Result 2:", result2)
print("Result 3:", result3)