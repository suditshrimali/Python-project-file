# Program to define and call user-defined functions with different types of arguments (positional, keyword, default, variable-length)

# Function with positional arguments
def nameAge(name, age):
    print("Hi, I am", name)
    print("I am", age, "years old.")
print("Case-1")
nameAge("Tony", 30)
print("\nCase-2")
nameAge(30, "Tony")  # This will work but the output will be incorrect

# Function with keyword arguments, using above function
print("\nCase-3")
nameAge(age=30, name="Tony")  # This will work correctly regardless of the order of arguments

# Function with default arguments
def greet(name, greeting="Hello"):
    print(greeting + ", " + name + "!")
print("\nCase-4")
greet("Tony")  # Uses default greeting
print("\nCase-5")
greet("Tony", greeting="Hi")  # Overrides default greeting

# Function with variable-length arguments
def sumNumbers(*numbers):
    total = sum(numbers)
    print("The sum of the numbers is:", total)
print("\nCase-6")
sumNumbers(1, 2, 3)  # Sums 1, 2, and 3
print("\nCase-7")
sumNumbers(4, 5)  # Sums 4 and 5