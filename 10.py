# Program to demonstrate string sclicing and built-in string methods

# String slicing
print("String slicing:")
s = "Hello, World!"
print(s[1:5])  # Output: ello
print(s[:5])   # Output: Hello
print(s[7:])   # Output: World!

# Built-in string methods
print("\nBuilt-in string methods:")

# Casing methods
print("Casing methods:")
print(s.upper())  # Output: HELLO, WORLD!
print(s.lower())  # Output: hello, world!
print(s.capitalize())  # Output: Hello, world!
print(s.title())  # Output: Hello, World!
print(s.swapcase())  # Output: hELLO, wORLD!

# Striping methods
print("Striping methods:")
s2 = "   Hello, World!   "
print(s2.strip())  # Output: Hello, World!
print(s2.lstrip())  # Output: Hello, World!
print(s2.rstrip())  # Output:    Hello, World!

# Searching methods
print("Searching methods:")
print(s.index("o"))  # Output: 4
print(s.rindex("o"))  # Output: 8
print(s.count("o"))  # Output: 2
print(min(s))  # Output: ' ' (space)
print(max(s))  # Output: 'r'
print(s.find("or"))  # Output: 7
print(s.rfind("o"))  # Output: 8

# Modifying methods
print("Modifying methods:")
print(s.replace("World", "Python"))  # Output: Hello, Python!
print('+'.join(s))  # Output: H+e+l+l+o+,+ +W+o+r+l+d+!
print(s.split(", "))  # Output: ['Hello', 'World!']

