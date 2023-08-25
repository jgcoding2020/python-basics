# For Loop
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Range-based For Loop
for i in range(1, 5):
    print(i)

# While Loop
count = 0
while count < 5:
    print(count)
    count += 1

# Break Statement
for i in range(1, 10):
    if i == 5:
        break
    print(i)

# Continue Statement
for i in range(1, 6):
    if i == 3:
        continue
    print(i)

# Nested Loops
for i in range(1, 4):
    for j in range(1, 4):
        print(f"({i}, {j})")

# Loop with Else
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    if fruit == "banana":
        print("Found banana!")
        break
else:
    print("No bananas found!")

# Infinite Loop (Caution: Use Ctrl+C to stop)
while True:
    print("This is an infinite loop!")

