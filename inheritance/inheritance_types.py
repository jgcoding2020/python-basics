# Base Class (Superclass)
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass


# Derived Class (Subclass) - Single Inheritance
class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"


class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"


# Create instances of derived classes
dog = Dog("Buddy")
cat = Cat("Whiskers")
print(dog.speak())
print(cat.speak())


# Multiple Inheritance
class Bird:
    def __init__(self, name):
        self.name = name

    def chirp(self):
        pass


class Parrot(Dog, Bird):
    def speak(self):
        return f"{self.name} says Squawk!"

    def chirp(self):
        return f"{self.name} chirps loudly!"


parrot = Parrot("Polly")
print(parrot.speak())
print(parrot.chirp())


# Multilevel Inheritance
class Mammal(Animal):
    def feed_milk(self):
        return f"{self.name} is a mammal and feeds milk."


class Dolphin(Mammal):
    def swim(self):
        return f"{self.name} is a dolphin and can swim."


dolphin = Dolphin("Flipper")
print(dolphin.speak())
print(dolphin.feed_milk())
print(dolphin.swim())


# Hierarchical Inheritance
class Lion(Mammal):
    def roar(self):
        return f"{self.name} is a lion and roars loudly."


class Elephant(Mammal):
    def trumpet(self):
        return f"{self.name} is an elephant and trumpets loudly."


lion = Lion("Simba")
elephant = Elephant("Dumbo")
print(lion.feed_milk())
print(lion.roar())
print(elephant.feed_milk())
print(elephant.trumpet())