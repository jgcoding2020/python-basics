from abc import ABC, abstractmethod


# Simple Class
class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello, my name is {self.name}."


# Create an instance of the Person class
person1 = Person("Alice")
print(person1.greet())


# Inheritance
class Student(Person):
    def __init__(self, name, student_id):
        super().__init__(name)
        self.student_id = student_id

    def study(self, subject):
        return f"{self.name} is studying {subject}."


# Create an instance of the Student class
student1 = Student("Bob", "12345")
print(student1.greet())
print(student1.study("Math"))


# Encapsulation
class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self._balance = balance  # Protected attribute

    def get_balance(self):
        return self._balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount


# Create an instance of the BankAccount class
account1 = BankAccount("123456", 1000)
print("Account Number:", account1.account_number)
print("Balance:", account1.get_balance())
account1.deposit(500)
print("New Balance after Deposit:", account1.get_balance())
account1.withdraw(200)
print("New Balance after Withdrawal:", account1.get_balance())


# Polymorphism
class Animal:
    def speak(self):
        pass


class Dog(Animal):
    def speak(self):
        return "Woof!"


class Cat(Animal):
    def speak(self):
        return "Meow!"


# Create instances of different animals
dog = Dog()
cat = Cat()
print(dog.speak())
print(cat.speak())


# Class Attributes and Methods
class Circle:
    pi = 3.14159  # Class attribute

    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return Circle.pi * self.radius**2


# Create instances of the Circle class
circle1 = Circle(5)
circle2 = Circle(3)
print("Circle 1 Area:", circle1.calculate_area())
print("Circle 2 Area:", circle2.calculate_area())


# Abstract Base Class (ABC)
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side**2


# Create an instance of the Square class
square = Square(4)
print("Square Area:", square.area())