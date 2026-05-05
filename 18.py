# Program to demonstrate file pointer manipulation using seek() and tell()

# Open the file in read mode
file = open('example.txt', 'r')
position = file.tell()
print('Initial file pointer position: ', position)

# Read the first 10 characters
print(file.read(10))
# Get the current position
position = file.tell()
print('Current file pointer position: ', position)

# Move the file pointer to the beginning of the file
file.seek(0)
# Read the first 5 characters
print(file.read(5))
# Get the current position
position = file.tell()
print('Current file pointer position: ', position)

# Move the file pointer to the end of the file
file.seek(0, 2)
# Get the current position of the file pointer
position = file.tell()
print('End of file pointer position: ', position)

# Close the file
file.close()