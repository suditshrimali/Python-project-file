# Program to demonstrate tuple creation, access, and immutability

# Creating a tuple
my_tuple = (1, 2, 3, 'Hello', 4.5)

# Accessing elements of the tuple
print("First element:", my_tuple[0])  # Output: 1
print("Fourth element:", my_tuple[3])  # Output: Hello

# Attempting to modify the tuple (Immutability demonstration)
try:
    my_tuple[1] = 10  # This will raise a TypeError
except TypeError as e:
    print("Error:", e)