# Program to demonstrate dictionary creation, insertion, deletion, update, and traversal

# Creating a dictionary
my_dict = {'name': 'Tony', 'age': 30, 'city': 'New York'}

# Accessing values in the dictionary
print("Name:", my_dict['name'])  # Output: Tony
print("Age:", my_dict['age'])    # Output: 30

# Inserting a new key-value pair
my_dict['profession'] = 'Engineer'
print("Updated Dictionary:", my_dict)

# Deleting a key-value pair
my_dict.pop('city')
print("Dictionary after deletion:", my_dict)

# Updating a value
my_dict['age'] = 31
print("Dictionary after update:", my_dict)

# Traversing the dictionary
print("\nKeys in the dictionary:")
for key in my_dict.keys():
    print(key)

print("\nValues in the dictionary:")
for value in my_dict.values():
    print(value)