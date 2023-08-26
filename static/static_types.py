class MathUtils:
    # Static Method 1: Basic static method
    @staticmethod
    def add(a, b):
        return a + b

    # Static Method 2: Static method with no arguments
    @staticmethod
    def hello_static():
        return "Hello from the static method!"


class Circle:
    # Class Attribute
    pi = 3.14159

    def __init__(self, radius):
        self.radius = radius

    # Static Method 3: Static method to create a circle
    @staticmethod
    def create_circle(radius):
        return Circle(radius)

    # Instance Method: Method to calculate the area of the circle
    def calculate_area(self):
        return Circle.pi * self.radius**2


# Using the static methods of MathUtils
result1 = MathUtils.add(5, 3)
greeting = MathUtils.hello_static()

print("Result 1:", result1)
print(greeting)

# Using the static method of the Circle class to create an instance
circle = Circle.create_circle(4)
print("Circle Radius:", circle.radius)

# Calculating the area of the circle using an instance method
area = circle.calculate_area()
print("Circle Area:", area)