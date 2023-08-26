from collections import namedtuple
from collections import deque

# Lists
my_list = [1, 2, 3, 4, 5]
print("List:", my_list)

# Tuples
my_tuple = (1, 2, 3, 4, 5)
print("Tuple:", my_tuple)

# Sets
my_set = {1, 2, 3, 4, 5}
print("Set:", my_set)

# Dictionaries
my_dict = {"name": "Alice", "age": 30, "city": "New York"}
print("Dictionary:", my_dict)

# Lists of Lists (2D List)
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("Matrix:", matrix)


# Stacks (Using Lists)
stack = []
stack.append(1)
stack.append(2)
stack.append(3)
popped = stack.pop()
print("Stack:", stack)
print("Popped Value:", popped)


# Queues (Using Lists)
queue = deque()
queue.append(1)
queue.append(2)
queue.append(3)
dequeued = queue.popleft()
print("Queue:", queue)
print("Dequeued Value:", dequeued)


# Linked Lists (Custom Implementation)
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


my_linked_list = LinkedList()
my_linked_list.append(1)
my_linked_list.append(2)
my_linked_list.append(3)
print("Linked List:")
my_linked_list.display()

# Dictionaries of Dictionaries
contacts = {
    "Alice": {"phone": "123-456-7890", "email": "alice@example.com"},
    "Bob": {"phone": "987-654-3210", "email": "bob@example.com"},
}
print("Contacts Dictionary:")
print(contacts)

# Sets of Sets
set_of_sets = {frozenset({1, 2, 3}), frozenset({4, 5, 6})}
print("Set of Sets:")
print(set_of_sets)

# NamedTuples
Person = namedtuple("Person", ["name", "age"])
person = Person("Alice", 30)
print("NamedTuple:", person)
