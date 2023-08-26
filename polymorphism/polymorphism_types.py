# Polymorphism through Method Overriding

# Base Class
class Animal:
    def speak(self):
        pass


# Derived Classes - Polymorphism through Method Overriding
class Dog(Animal):
    def speak(self):
        return "Woof!"


class Cat(Animal):
    def speak(self):
        return "Meow!"


# Create instances of different animals
dog = Dog()
cat = Cat()

# Calling the speak method on different objects
print(dog.speak())
print(cat.speak())

# Polymorphism with a Common Interface


# Interface
class Drawable:
    def draw(self):
        pass


# Classes Implementing the Interface
class Circle(Drawable):
    def draw(self):
        return "Drawing a circle"


class Rectangle(Drawable):
    def draw(self):
        return "Drawing a rectangle"


# Create instances of different shapes
circle = Circle()
rectangle = Rectangle()

# Calling the draw method on different shapes
print(circle.draw())
print(rectangle.draw())

# Polymorphism with Built-in Functions

# Polymorphism with len() on different data types
string_length = len("Hello, World!")
list_length = len([1, 2, 3, 4, 5])
dict_length = len({"a": 1, "b": 2, "c": 3})

print("String Length:", string_length)
print("List Length:", list_length)
print("Dictionary Length:", dict_length)

# Polymorphism with + operator on different data types
result1 = 5 + 10
result2 = "Hello, " + "World!"
result3 = [1, 2, 3] + [4, 5, 6]

print("Result 1:", result1)
print("Result 2:", result2)
print("Result 3:", result3)


# Polymorphism with Built-in Functions and Operators
def calculate_area(shape):
    return shape.calculate_area()


# Base Class with a Common Method
class Shape:
    def calculate_area(self):
        pass


# Derived Classes with Method Implementation
class Circle(Shape):
    def calculate_area(self):
        return 3.14159 * self.radius**2


class Square(Shape):
    def calculate_area(self):
        return self.side**2


# Create instances of different shapes
circle = Circle()
circle.radius = 5
square = Square()
square.side = 4

# Calculate and display the areas using polymorphism
print("Circle Area:", calculate_area(circle))
print("Square Area:", calculate_area(square))