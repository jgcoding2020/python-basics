# Decorator Function
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper


# Applying a Decorator to a Function
@my_decorator
def say_hello():
    print("Hello!")


say_hello()


# Decorator with Arguments
def repeat_n_times(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator


# Applying a Decorator with Arguments
@repeat_n_times(3)
def greet(name):
    print(f"Hello, {name}!")


greet("Alice")


# Class-Based Decorator
class MyDecoratorClass:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print("Something is happening before the function is called.")
        self.func(*args, **kwargs)
        print("Something is happening after the function is called.")


@MyDecoratorClass
def say_goodbye():
    print("Goodbye!")


say_goodbye()


# Built-in Decorators
@staticmethod
def static_example():
    print("This is a static method.")


static_example()


@classmethod
def class_method_example(cls):
    print(f"This is a class method of {cls.__name__}.")


class_method_example()

# Decorator for Authorization
user_authenticated = True  # Simulate user authentication


def require_authentication(func):
    def wrapper(*args, **kwargs):
        if user_authenticated:
            func(*args, **kwargs)
        else:
            print("Authentication required.")
    return wrapper


@require_authentication
def view_sensitive_data():
    print("This is sensitive data.")


view_sensitive_data()
