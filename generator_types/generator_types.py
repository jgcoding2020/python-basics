# Generator Expression to Create a Generator
squares_generator = (x ** 2 for x in range(1, 6))
print("Squares Generator (Expression):", squares_generator)

# Using a Generator to Iterate and Calculate Sum
squares_sum = sum(x for x in range(1, 6))
print("Sum of Squares (Expression):", squares_sum)


# Generator Function for Fibonacci Sequence
def fibonacci_generator(n):
    a, b = 0, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1


# Using the Fibonacci Generator
fibonacci_sequence = list(fibonacci_generator(10))
print("Fibonacci Sequence (Function):", fibonacci_sequence)


# Generator Function for Prime Numbers
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def prime_generator(limit):
    for number in range(2, limit):
        if is_prime(number):
            yield number


# Using the Prime Number Generator
prime_numbers = list(prime_generator(30))
print("Prime Numbers (Function):", prime_numbers)


# Infinite Generator Function
def infinite_counter():
    count = 0
    while True:
        yield count
        count += 1


# Using the Infinite Generator
counter = infinite_counter()
for _ in range(5):
    print(next(counter))


# Generator Function with 'return' to Stop Iteration
def limited_generator(n):
    for i in range(n):
        yield i
    return "Done"


gen = limited_generator(3)
for item in gen:
    print(item)
try:
    next(gen)
except StopIteration as e:
    print("Generator stopped:", e.value)
