# Public, Protected, and Private Attributes

class Student:
    def __init__(self, name, roll_number):
        self.name = name  # Public attribute
        self._roll_number = roll_number  # Protected attribute
        self.__marks = {}  # Private attribute

    def set_marks(self, subject, score):
        self.__marks[subject] = score

    def get_marks(self, subject):
        return self.__marks.get(subject, "Subject not found")


# Create an instance of the Student class
student1 = Student("Alice", "S123")
student1.set_marks("Math", 90)
student1.set_marks("Science", 85)

# Accessing public attributes
print("Name:", student1.name)

# Accessing protected attribute (convention)
print("Roll Number:", student1._roll_number)

# Accessing private attribute (name mangling)
# This is not recommended and should be avoided.
# Use public methods to access private attributes.
print("Marks:", student1._Student__marks)

# Using public method to access private attribute
print("Math Score:", student1.get_marks("Math"))
print("History Score:", student1.get_marks("History"))


# Property and Setter Methods

class Temperature:
    def __init__(self):
        self._celsius = 0

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            print("Temperature can't be less than -273.15°C")
        else:
            self._celsius = value


# Create an instance of the Temperature class
temp = Temperature()

# Accessing the property
print("Temperature in Celsius:", temp.celsius)

# Setting the property using the setter method
temp.celsius = 25
print("New Temperature in Celsius:", temp.celsius)

# Attempting to set an invalid temperature
temp.celsius = -300


# Property Deletion

class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def info(self):
        return f"{self._name} is {self._age} years old."

    @info.deleter
    def info(self):
        print("Person's info is deleted.")
        del self._name
        del self._age


# Create an instance of the Person class
person = Person("Alice", 30)

# Accessing the property
print(person.info)

# Deleting the property
del person.info

# Attempting to access the property after deletion
# This should raise an error because the attributes are deleted
print(person.info)

