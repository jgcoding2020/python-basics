# Basic Function
def greet():
    print("Hello, World!")


greet()


# Function with Parameters
def add(x, y):
    return x + y


result = add(3, 5)
print("Addition Result:", result)


# Function with Default Arguments
def greet_person(name="Guest"):
    print(f"Hello, {name}!")


greet_person()
greet_person("Alice")


# Function with Variable-Length Arguments (*args)
def print_args(*args):
    for arg in args:
        print(arg)


print_args(1, 2, 3, "four", "five")


# Function with Keyword Arguments (**kwargs)
def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


print_kwargs(name="Alice", age=30, city="New York")


# Regular Function (not lambda)
def square(x):
    return x**2


result = square(5)
print("Square Result:", result)


# Function with Docstring
def show_docstring():
    """
    This is a docstring.
    It provides information about the function.
    """
    print("Function with a docstring")


help(show_docstring)  # Display the docstring