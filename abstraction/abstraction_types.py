from abc import ABC, abstractmethod


# Abstract Base Class (ABC) with Abstract Method
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


# Concrete Classes Implementing the Abstract Method
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius**2


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side**2


# Create instances of the concrete classes
circle = Circle(5)
square = Square(4)

# Calling the abstract method through the instances
print("Circle Area:", circle.area())
print("Square Area:", square.area())


# Abstract Base Class (ABC) with Concrete Methods
class Animal(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def speak(self):
        pass

    def info(self):
        return f"{self.name} is an animal."


# Concrete Classes Implementing Abstract and Concrete Methods
class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"


class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"


# Create instances of the concrete classes
dog = Dog("Buddy")
cat = Cat("Whiskers")

# Calling both abstract and concrete methods
print(dog.info())
print(cat.speak())


# Abstraction in Interfaces
class Drawable(ABC):
    @abstractmethod
    def draw(self):
        pass


# Implementing the Interface
class Circle(Drawable):
    def draw(self):
        return "Drawing a circle"


class Rectangle(Drawable):
    def draw(self):
        return "Drawing a rectangle"


# Create instances of the classes implementing the interface
circle = Circle()
rectangle = Rectangle()

# Calling the draw method through the instances
print(circle.draw())
print(rectangle.draw())
