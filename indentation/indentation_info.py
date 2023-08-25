# Single-level indentation
def single_level_indentation():
    print("This is a single-level indentation block.")
    print("It contains two statements.")


single_level_indentation()


# Nested indentation
def nested_indentation():
    print("This is the outer block.")
    print("It contains an inner block.")
    if True:
        print("This is the inner block.")
        print("Nested indentation is used for deeper levels of code.")


nested_indentation()


# Conditional indentation
def conditional_indentation(x):
    if x > 5:
        print("x is greater than 5.")
        print("This code is indented under the 'if' statement.")
    else:
        print("x is not greater than 5.")
        print("This code is indented under the 'else' statement.")


conditional_indentation(7)
conditional_indentation(3)


# Loop indentation
def loop_indentation():
    for i in range(3):
        print("This is inside the loop.")
    print("This is outside the loop.")


loop_indentation()


# Function indentation
def function_indentation():
    def inner_function():
        print("This is inside the inner function.")

    print("This is inside the outer function.")
    inner_function()
    print("This is outside the outer function.")


function_indentation()


# Class indentation
class MyClass:
    def __init__(self):
        self.value = 42

    def display_value(self):
        print("The value is:", self.value)


my_instance = MyClass()
my_instance.display_value()
